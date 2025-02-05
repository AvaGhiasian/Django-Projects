from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page, name="start-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_details, name="post-detail-page")
]
