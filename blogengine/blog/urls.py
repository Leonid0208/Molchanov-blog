from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_details'),
    path('post/<str:slug>/edit/', PostEdit.as_view(), name='post_edit_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tags_list, name='tags_lists'),
    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>/', TagDetail.as_view(), name='tag_details'),
    path('tags/<str:slug>/edit/', TagEdit.as_view(), name='tag_edit_url'),
    path('tags/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),

    path('post/', post_redirect),
]