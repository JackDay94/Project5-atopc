from django.urls import path
from .views import PostList, PostDetail, AddPost, EditPost, DeletePost

urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/edit_post/', EditPost.as_view(), name='edit_post'),
    path('<slug:slug>/delete_post/', DeletePost.as_view(), name='delete_post'),

]
