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
    path('Bibbirria/', views.Bibbirria, name='Bibbirria'),
    path('Chiesa-San-Nicola/', views.ChiesaSanNicola, name='ChiesaSanNicola'),
    path('rabato/', views.Rabato, name='Rabato'),


   
]