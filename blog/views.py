from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm,CommentForm
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView


# Create your views here.






class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostList(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(publish_time__lte=timezone.now()).order_by('-publish_time')


class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin,CreateView):
    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class =PostForm
    model = Post

class PostEdit(LoginRequiredMixin,UpdateView):
    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class =PostForm

    model = Post


class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list') 


class PostDraft(LoginRequiredMixin,ListView):
    login_url = "/login/"
    redirect_field_name="blog/post_list.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_time__isnull=True).order_by('create_time')



@login_required
def publish_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', pk=post.pk)

    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {'form': form})



@login_required
def approve_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)


@login_required
def delete_comment(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

    
    

