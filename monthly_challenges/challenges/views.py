from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "January": "Complete a 30-day coding challenge on LeetCode.",
    "February": "Contribute to an open-source project on GitHub.",
    "March": "Build and deploy a personal website or portfolio.",
    "April": "Learn a new programming language or framework.",
    "May": "Write a technical blog on a topic you're passionate about.",
    "June": "Develop and launch a small mobile or web app.",
    "July": "Participate in a hackathon or coding competition.",
    "August": "Read and implement a research paper in your field.",
    "September": "Optimize an old project for performance improvements.",
    "October": "Speak at a local meetup or create a tutorial video.",
    "November": "Automate a daily task using a script or bot.",
    "December": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})
    

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
        print(challenge_text)
        print(month)
        return render(request,"challenges/challenge.html", {"month": month, "challenge_description": challenge_text})
    except:
        return HttpResponseNotFound("invalid month")