from django.db import models

class Usuari(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    correu = models.EmailField(unique=True)
    contrasenya = models.CharField(max_length=100)
    data_creacio = models.DateTimeField(auto_now_add=True)
