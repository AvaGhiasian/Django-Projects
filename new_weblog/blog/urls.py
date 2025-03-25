from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts_list, name='all_posts'),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
]
