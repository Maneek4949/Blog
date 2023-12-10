from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User,auth
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    publish_time = models.DateTimeField(blank=True,null=True)
    cover_image = models.ImageField(upload_to='blog_cover',blank=True)
    likes = models.ManyToManyField(User, through='Like', related_name='liked_posts')
    disabled = models.BooleanField(default=False)
    
    def publish(self):
        self.publish_time = timezone.now()
        self.save()

    def enable(self):
        self.disabled = False
        self.save()
    def disable(self):
        self.disabled = True
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    text = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    approved_comments= models.BooleanField(default=False)
    def approve(self):
        self.approved_comments = True
        self.save()

    def __str__(self):
        return self.post




class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.IntegerField(default=0) 



