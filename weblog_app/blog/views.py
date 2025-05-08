from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.

def index(request):
    # last_post = Post.published.all().order_by('-publish')[0]
    # context = {
    #     "last_post": last_post
    # }
    # return render(request, "blog/index.html", context)
    return render(request, 'blog/index.html')


# def post_list(request, category=None):
#     posts = Post.published.all()
#     paginator = Paginator(posts, 5)
#     page_number = request.GET.get('page', 1)
#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)  # shows the last page
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#
#     context = {
#         'posts': posts,
#     }
#     return render(request, "blog/list.html", context)

class PostListView(ListView):
    # model = Post  by default takes Post.objects.all()
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = "blog/list.html"

# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
#     context = {
#         'post': post,
#     }
#     return render(request, "blog/detail.html", context)

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
