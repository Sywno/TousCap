from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model()

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile', null=True)
    is_client = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name

class Benevole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='benevole_profile', null=True)
    is_benevole = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
    
    
class Agenda(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nom_utilisateur = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    lieu = models.CharField(max_length=100)
    heure = models.TimeField()
    commentaire = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_utilisateur + " - " + str(self.tel) + " - " + str(self.email) + " - " + str(self.date) + " - " + str(self.heure) + " - " + str(self.lieu)
