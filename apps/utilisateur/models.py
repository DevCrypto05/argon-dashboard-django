from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Utilisateur(models.Model):
    roles = [("Admin", "Admin"), ("Simple", "Simple")]
    Nom = models.CharField(max_length=50, blank=True, null=False)
    Prenom = models.CharField(max_length=50, blank=True, null=False)
    Role = models.CharField(max_length=10, blank=True, choices=roles, default="Simple")
    Image = models.ImageField(upload_to="image_user")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    