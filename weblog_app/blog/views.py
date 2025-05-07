from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Post


# Create your views here.

def index(request):
    # last_post = Post.published.all().order_by('-publish')[0]
    # context = {
    #     "last_post": last_post
    # }
    # return render(request, "blog/index.html", context)
    return render(request, 'blog/index.html')


def post_list(request, category=None):
    posts = Post.published.all()
    context = {
        'posts': posts,
    }
    return render(request, "blog/list.html", context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    context = {
        'post': post,
    }
    return render(request, "blog/detail.html", context)
