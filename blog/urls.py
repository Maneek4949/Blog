from django.urls import path
from blog import views 


urlpatterns=[
    path('',views.PostList.as_view(),name='post_list'),
    path('post/<int:pk>',views.PostDetail.as_view(),name='post_detail'),
    path('post/create/',views.PostCreate.as_view(),name='create'),
    path('post/<int:pk>/edit/',views.PostEdit.as_view(),name='edit'),
    path('post/<int:pk>/delete/',views.PostDelete.as_view(),name='delete'),
    path('draft/',views.PostDraft.as_view(),name='draft'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>/comment/',views.add_comment,name='add_comment'),
    path('post/<int:pk>/approve/',views.approve_comment,name='approve_comment'),
    path('post/<int:pk>/delete/',views.delete_comment,name='delete_comment'),
    path('post/<int:pk>/publish/',views.publish_post,name='publish'),
]