from django.urls import path
from blog import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.PostList.as_view(),name='post_list'),
    path('my',views.MyPost.as_view(),name='my_post'),
    path('draft/',views.PostDraft.as_view(),name='draft'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/create/',views.PostCreate.as_view(),name='create'),
    path('post/<int:pk>/',views.PostDetail.as_view(),name='post_detail'),
    path('post/<int:pk>/publish/',views.publish_post,name='publish'),
    path('post/<int:pk>/edit/',views.PostEdit.as_view(),name='edit'),
    path('post/<int:pk>/delete/',views.PostDelete.as_view(),name='delete'),
    path('comment/<int:pk>/approve/',views.approve_comment,name='approve_comment'),
    path('comment/<int:pk>/delete/',views.delete_comment,name='delete_comment'),
    path('check_email_availability/', views.check_email_availability, name='check_email_availability'),
    path('post/<int:pk>/enable/', views.enable_post, name='enable_post'),
    path('post/<int:pk>/disable/', views.disable_post, name='disable_post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)