from django.urls import path
from .views import NewPost, DeletePost

urlpatterns = [
    path('posts/', NewPost.as_view(), name="create-post"),
    path('posts/delete/<int:pk>/', DeletePost.as_view(), name="delete-post")
]