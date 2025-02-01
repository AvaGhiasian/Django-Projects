from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn django for at least 20 minutes every day!",
    "april": "Drink 8 cups of water a day!",
    "may": "Eat an apple a day!",
    "june": "Study for 5 hours every day!",
    "july": "Get 8 hours of sleep every day!",
    "august": "Eat vegtables!",
    "september": "Run 30 minutes every day!",
    "october": "Swim for at least 1 hour every week!",
    "november": "Ride a bicycle for at least 20 minutes every day!",
    "december": "Visit family for at least 20 minutes every other day!"
}

def index(request):
    list_items = ""
    months = list(challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenges", args=[month ])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenges(request, month: str):
    try:
        challenge_txt = challenges[month]
        return render(request, "challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")


def monthly_challenges_by_num(request, month: int):
    try:
        months = list(challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse(
            "month-challenges", args=[redirect_month])  # /challange/
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month is not supoorted!")

    """
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This month is not supoorted!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenges", args=[redirect_month]) #/challange/
    return HttpResponseRedirect(redirect_path)
    """
