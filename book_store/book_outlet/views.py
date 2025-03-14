from django.shortcuts import render, get_object_or_404
from . models import Book
from django.http import Http404
from django.db.models import Avg, Max, Min

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("title") # title = ascending order , -title = descending order
    total_no_of_books = books.count()
    rating = books.aggregate(Avg("rating"), Min("rating"), Max("rating"))


    return render(request, "book_outlet/index.html", {
            "books": books,
            "total_no_of_books": total_no_of_books,
            "rating": rating,
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_best_selling": book.is_best_selling,
    })
