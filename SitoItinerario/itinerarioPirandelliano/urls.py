from django.urls import path
from . import views

#qui devi aggiungere path('nome che vuoi dopo /home/', views.nome della vista),
urlpatterns = [
    
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('PianoSanGerlando/', views.PianoSanGerlando, name='PianoSanGerlando'),
    path('Basilica-Immacolata/', views.Basilica, name='Basilica'),
    path('Cattedrale-Palazzo-Vescovile/', views.Cattedrale, name='Cattedrale'),
    path('Viale-Vittoria/', views.VialeVittoria, name='VialeVittoria'),
    path('Casa-Pirandello/', views.Pirandello, name='Pirandello'),
    path('CasaRavanusella/', views.CasaRavanusella, name='CasaRavanusella'),
    path('Rabato/', views.Rabato, name='Rabato'),


   
]