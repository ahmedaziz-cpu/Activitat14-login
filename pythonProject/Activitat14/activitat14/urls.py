from django.urls import path
from . import views

app_name = 'activitat14'

urlpatterns = [
    path('', views.inici, name='inici'),
    path('login/', views.login_vista, name='login_vista'),
]
