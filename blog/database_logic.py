from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User,auth
from blog.models import Comment


# this function is used to delete the pk comment from the post
def deleting_comment(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.post.author:
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)
    else:
        return HttpResponseForbidden("You do not have permission to delete this comment.")


# save_comment saves comment information to the database.
def save_comment(request, form, post):
    comment = form.save(commit=False)
    comment.post = post
    comment.author = request.user.username
    comment.save()

# save_post saves post information to the database.
def save_post(request, form):
    form.instance.author = request.user
    form.save()

#save_user saves user information to the database.
def save_user(first_name,last_name,email,password):
    user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)
    user.save()
