from django.urls import path
from ..vente import views

urlpatterns = [
    path('icon', views.icon, name='icon'),
    path('categorie', views.categorie, name='categorie')
]
