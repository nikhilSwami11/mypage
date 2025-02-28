from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

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
    "December": "Reflect on your year's progress and set goals for next year."
}


def index(request):
    list_items = []
    months = list(monthly_challenges.keys())
    for month in months:
        link = reverse("month-challenge", args = [month])
        list_item = f' <li><a href ="{link}">{month}</a></li> '
        list_items.append(list_item)
    combinedListString = "" 
    for value in list_items:
        combinedListString += value
    return HttpResponse(f" <ul>{combinedListString}</ul>")
    

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
        return render(request,"challenges/challenge.html", {"month": month, "challenge_description": challenge_text})
    except:
        return HttpResponseNotFound("This month is not supported")