from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User,auth
from .models import Comment,Post,Like




#process_comment_approval approves a comment with a given pk(id).

def process_comment_approval(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.post.author:
        comment.approve()
        return redirect('post_detail', pk=comment.post.pk)
    else:
        return HttpResponseForbidden("You do not have permission to approve this comment.")

#process_publish_post approves a draft post with a given pk(id).
def process_publish_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()


#form_datas getting the values from register form

def form_datas(request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password'].strip()
        return {'first_name':first_name,'last_name':last_name,'email':email,'password':password}


#check_user check's that user is in our database or not
def check_user(request):
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('post_list')
        else:
            return redirect('login')


def process_like_dislike(request, post, value):
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        like.value = value
        like.save()
        post.likes.add(request.user)
    elif like.value != value:
        like.value = value
        like.save()
    else:
        like.delete()
        post.likes.remove(request.user)