from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def page_utilisateur(request):
    # context = {}
    # return render(request, "home/profiles.html", context)
    template = loader.get_template("home/profile.html")
    context = {
        "latest_question_list": "latest_question_list",
    }
    return HttpResponse(template.render(context, request))

# def creation_user(request):