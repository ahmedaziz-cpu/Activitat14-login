from django.contrib import admin

from .models import Usuari


# Register your models here.
@admin.register(Usuari)
class login(admin.ModelAdmin):
    list_display = ('id', 'nom' , 'correu' , 'contrasenya', 'data_creacio')