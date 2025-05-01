from django.db import models


class Usuario(models.Model):
    username = models.CharField(max_length=500, unique=True)
    email = models.EmailField(max_length=500)
    nombre = models.CharField(max_length=500)
    apellido = models.CharField(max_length=500)
    password = models.CharField(max_length=500, null=False)
