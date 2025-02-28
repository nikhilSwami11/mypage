from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat",
    'february': "No dairy this month!",
    'march': "Study for 40 hours in a week!",
    "april": "hii h",
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args = [redirect_month]) # this will automatically detect the path
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    challenge_text = None
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)