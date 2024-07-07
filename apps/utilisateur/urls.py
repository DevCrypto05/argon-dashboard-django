from django.urls import path
from apps.utilisateur import views

urlpatterns = [
    path('profile', views.page_utilisateur, name="profile")
]
