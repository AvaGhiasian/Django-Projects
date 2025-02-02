from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


challenges = {
    "january": "Eat no meat for the entire month!",
    "february": None,
    "march": "Learn django for at least 20 minutes every day!",
    "april": "Drink 8 cups of water a day!",
    "may": "Eat an apple a day!",
    "june": "Study for 5 hours every day!",
    "july": "Get 8 hours of sleep every day!",
    "august": "Eat vegetables!",
    "september": None,
    "october": "Swim for at least 1 hour every week!",
    "november": "Ride a bicycle for at least 20 minutes every day!",
    "december": "Visit family for at least 20 minutes every other day!"
}

def index(request):
    list_items = ""
    months = list(challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenges(request, month: str):
    try:
        challenge_txt = challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_txt,
            "month_name": month.capitalize()
            })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

def monthly_challenges_by_num(request, month: int):
    try:
        months = list(challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse(
            "month-challenges", args=[redirect_month])  # /challenge/
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month is not supported!")

    """
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This month is not supported!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenges", args=[redirect_month]) #/challenge/
    return HttpResponseRedirect(redirect_path)
    """
