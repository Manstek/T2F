from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
     path('', views.PostListView.as_view(), name='index'),
     path('create/', views.PostCreateView.as_view(), name='create'),
     path('post/<int:post_id>/', views.PostDetailView.as_view(), name='detail'),
     path('group/<slug:slug>/', views.GroupDetailView.as_view(), name='group'),
     path('group_list/', views.GroupListView.as_view(), name='group_list'),

     path('profile/edit/',
          views.ProfileUpdateView.as_view(),
          name='edit_profile'),

     path('profile/<str:username>/',
          views.ProfileDetailView.as_view(),
          name='profile'),

     path('posts/<int:post_id>/comment/',
          views.CommentCreateView.as_view(),
          name='add_comment'),

     path('posts/<int:post_id>/comment/<int:comment_id>/delete',
          views.CommentDeleteView.as_view(),
          name='delete_comment'),

     path('posts/<int:post_id>/comment/<int:comment_id>/edit',
          views.CommentUpdateView.as_view(),
          name='edit_comment'),

     path('posts/<int:post_id>/edit/',
          views.PostUpdateView.as_view(),
          name='edit'),

     path('posts/<int:post_id>/delete/',
          views.PostDeleteView.as_view(),
          name='delete'),

     path('posts/<int:post_id>/like/',
          views.LikeCreateView.as_view(),
          name='like'),

     path('posts/<int:post_id>/unlike/',
          views.LikeDeleteView.as_view(),
          name='unlike'),

]
