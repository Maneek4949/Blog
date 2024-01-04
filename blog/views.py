from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from blog.models import Post,Comment,Like
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.forms import PostForm,CommentForm,LikeForm
from django.views import View
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User,auth
from django.http import JsonResponse, HttpResponseForbidden

from .bussiness_logic import process_comment_approval,process_publish_post,form_datas,check_user,process_like_dislike
from .database_logic import deleting_comment,save_comment,save_post,save_user

# Create your views here.


#AboutView displays information about the blog.
class AboutView(TemplateView):
    template_name = 'blog/about.html'


#PostList displays List of all post by all user
class PostList(LoginRequiredMixin,ListView):
    login_url = ""
    model = Post
    def get_queryset(self):
        return Post.objects.filter(publish_time__lte=timezone.now(),enabled=True).order_by('-publish_time')

#MyPost displays Lists of single User Post only
class MyPost(ListView):
    template_name='blog/my_post.html'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(publish_time__lte=timezone.now()).order_by('-publish_time')

class Permission(UserPassesTestMixin):
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or post.enabled

    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to access this post.")


#PostDetail displays the details of post with pk id
class PostDetail(Permission,DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        like_form = LikeForm()
        like = Like.objects.filter(post=post, user=request.user).values()
        form = CommentForm()
        return render(request, self.template_name, {'post': post, 'form': form, 'like_form': like_form, 'status': like})
        

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form = CommentForm(request.POST)
        like_form = LikeForm(request.POST)

        if form.is_valid():
            save_comment(request, form, post)
            return redirect('post_detail', pk=post.pk)

        if like_form.is_valid() and request.user.is_authenticated:
            process_like_dislike(request, post, like_form.cleaned_data['value'])
            return redirect('post_detail', pk=post.pk)

        return render(request, self.template_name, {'post': post, 'form': form, 'like_form': like_form})


#PostCreate create new post 
class PostCreate(CreateView):
    login_url = ""
    redirect_field_name = "blog/post_detail.html"
    model = Post
    form_class = PostForm
    def form_valid(self, form):
        save_post(self.request,form)
        return super().form_valid(form)

#PostEdit edit or upadate existing posts
class PostEdit(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    login_url = ""
    redirect_field_name = "blog/post_detail.html"
    model = Post
    form_class = PostForm
    def test_func(self):
        if self.get_object().author != self.request.user:
             raise PermissionDenied("You do not have permission to edit this post.")
        return True
    
    def form_valid(self,form_class):
        response = super().form_valid(form_class)
        return response

#PostDelete delete the existing posts
class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    login_url = ""
    template_name='blog/post_detail.html'
    model = Post
    success_url = reverse_lazy('post_list')
    def test_func(self):
        if self.get_object().author != self.request.user:
             raise PermissionDenied("You do not have permission to delete this post.")
        return True

#PostDraft displays the incomplete Post of User
class PostDraft(LoginRequiredMixin,ListView):
    login_url = ""
    redirect_field_name="blog/post_list.html"
    model = Post
    def get_queryset(self):
        return Post.objects.filter(publish_time__isnull=True).order_by('create_time')



#publish_post for publishes a post with a given pk.
@login_required(login_url='/') 
def publish_post(request,pk):
    process_publish_post(request,pk)
    return redirect('post_detail',pk=pk)


#enable_post for enabling the post
def enable_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.enable()
    return render(request, 'blog/post_detail.html', {'post': post})

#disable_post for disabling the post
def disable_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.user == post.author:
        post.disable()
    return render(request, 'blog/post_detail.html', {'post': post})



#approve_cooment approves comment's those the done by other users on user post
@login_required
def approve_comment(request, pk):
    return process_comment_approval(request,pk)
    
#delete_comment delete the comment's those the done by other users on user post
@login_required
def delete_comment(request, pk):
    return deleting_comment(request,pk)
    
#login display login form to Singin Registerd Users
def login(request):
    if request.method =='POST':
        return check_user(request)
    else:
        return render(request,'registration/login.html')


#register displays Register form for new user
def register(request):
    if request.method == 'POST':
        user = form_datas(request)
        save_user(user['first_name'],user['last_name'],user['email'],user['password'])
        return redirect('post_list')

    else:
        return render(request, 'registration/register.html')

def check_email_availability(request):
    email = request.GET.get('email', None)
    data = {'available': not User.objects.filter(email=email).exists()}
    return JsonResponse(data)




