from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def review(request):
    """
    method gives access to the method that was used for submitting the data
    .POST gives access to the data itself
    POST is a dict where keys are the names sat on the inputs in the form,
    and values are the entered values
    post req is meant to submit data to the server, 
    instead of returning a rendered template we redirect to a different url with get req
    and that url will render a template

    """
    if request.method == "POST":
        entered_username = request.POST["username"]

        if entered_username == "" and len(entered_username) >= 100:
            return render(request, "reviews/review.html", {
                "has_error": True
            })
        
        return HttpResponseRedirect("/thank-you")

    return render(request, "reviews/review.html", {
        "has_error": False
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
