from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = 'blog'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Blog Posts (CRUD) → note: **singular "post/"**
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]


from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentUpdateView, CommentDeleteView
)

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),

    # Auth
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Posts (note singular 'post/')
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments (create happens via PostDetailView POST, update/delete separate)
    # edit a comment
    path('post/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    # delete a comment
    path('post/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]


from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    # Create a new comment
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment'),

    # Edit a comment
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),

    # Delete a comment
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]
