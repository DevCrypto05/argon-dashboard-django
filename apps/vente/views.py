from django.shortcuts import render

# Create your views here.

def icon(request):
    return render(request, "home/icons.html")

def categorie(request):
    return render(request, "home/categorie.html")

def caisse(request):
    return render(request, "home/caisse.html")

def commande(request):
    return render(request, "home/commande.html")

def menu(request):
    return render(request, "home/menu.html")

def table(request):
    return render(request, "home/tables.html")

def historique(request):
    return render(request, "home/historique.html")