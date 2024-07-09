from django.urls import path
from ..vente import views

urlpatterns = [
    path('icon', views.icon, name='icon'),
    path('categorie', views.categorie, name='categorie'),
    path('caisses', views.caisse, name='caisses'),
    path('commande', views.commande, name='commande'),
    path('menu', views.menu, name='menu'),
    path('table', views.table, name='table'),
    path('historique', views.historique, name='historique'),
]
