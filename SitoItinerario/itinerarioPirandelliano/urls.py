from django.urls import path
from . import views

#qui devi aggiungere path('nome che vuoi dopo /home/', views.nome della vista),
urlpatterns = [
    path('', views.home, name='home'),
   
]