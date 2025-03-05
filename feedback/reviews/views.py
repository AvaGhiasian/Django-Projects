from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })


"""def review(request):
    method gives access to the method that was used for submitting the data
    .POST gives access to the data itself
    POST is a dict where keys are the names sat on the inputs in the form,
    and values are the entered values
    post req is meant to submit data to the server, 
    instead of returning a rendered template we redirect to a different url with get req
    and that url will render a template

    if request.method == "POST":
        entered_username = request.POST["username"] .POST gives us access to the key

        if entered_username == "" and len(entered_username) >= 100:
            return render(request, "reviews/review.html", {
                "has_error": True
            })

        return HttpResponseRedirect("/thank-you")

    return render(request, "reviews/review.html", {
        "has_error": False
    })

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            
            form.is_valid() is defines in Form class and does 3 things:
            1- validating the input(checking if it is not empty)
            2- returns true if form is valid
            3- if data is valid, it'll populate another field with that valid data
            
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        else it is a GET request: 
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })
"""


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This Works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    """
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data
    """


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # review_id gets stored in the session with the key: favorite_review
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
