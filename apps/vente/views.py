from django.shortcuts import render

# Create your views here.

def icon(request):
    return render(request, "home/icons.html")

def categorie(request):
    return render(request, "home/categorie.html")