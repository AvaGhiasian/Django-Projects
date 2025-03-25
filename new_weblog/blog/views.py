from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post


# Create your views here.


def index(request):
    return HttpResponse("Hello, world.")


def posts_list(request):
    posts = Post.published.all()
    context = {
        'posts': posts
    }
    return render(request, "blog/list.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)

    context = {
        'post': post
    }
    return render(request, "blog/detail.html", context)
