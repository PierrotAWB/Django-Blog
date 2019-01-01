from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView, 
    PostDeleteView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    # pk is a primary key
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # a create view looks at a different location; 
    # rather than check blog/post_create.html as you might
    # guess, it looks for blog/post_form.html. Note that this
    # is shared by the Update view.
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about')
]