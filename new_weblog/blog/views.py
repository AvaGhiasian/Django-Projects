from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST
from .forms import TicketForm, CommentForm
from .models import Post, Ticket


# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "blog/list.html"


class PostDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': comments,
    }
    return render(request, 'blog/detail.html', context)


def index(request):

    return render(request, 'blog/index.html')


def ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_obj = Ticket.objects.create()
            cleaned_data = form.cleaned_data
            ticket_obj.message = cleaned_data['message']
            ticket_obj.name = cleaned_data['name']
            ticket_obj.email = cleaned_data['email']
            ticket_obj.phone = cleaned_data['phone']
            ticket_obj.subject = cleaned_data['subject']
            ticket_obj.save()
            return redirect('blog/index')
    else:
        form = TicketForm()
    return render(request, "forms/ticket.html", {'form': form})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    context = {
        'post': post,
        'comment': comment,
        'form': form,
    }
    return render(request, "forms/comment.html", context)
