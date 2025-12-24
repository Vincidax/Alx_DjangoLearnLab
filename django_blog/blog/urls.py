from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register,
    profile,
    home,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),           # singular 'post'
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # checker expects 'update'
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-add'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]