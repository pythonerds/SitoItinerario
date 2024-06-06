from django.shortcuts import render,redirect
from django.utils.translation import activate
#from django.utils.translation import gettext_lazy as _
from django.conf import settings
import logging
from django.urls import reverse,resolve

# Configura il logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Configura il gestore di log per scrivere su console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Configura il formato del log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Aggiungi il gestore di log al logger
logger.addHandler(console_handler)



def home(request):
    pagina="home"


    logger.debug(f"----------Contenuto della sessione: {request.session.items()}")
    #paragrafo=_("paragrafo")
    return render(request, 'itinerarioPirandelliano/home.html',{"pagina":pagina})

def PianoSanGerlando(request):
    pagina="PianoSanGerlando"
    language = request.LANGUAGE_CODE


    logger.debug(f"----------Contenuto della sessione: {request.session.items()}")
    #paragrafo=_("paragrafo")
    return render(request, 'itinerarioPirandelliano/PianoSanGerlando.html',{"pagina":pagina, "lang_name":language})

def Basilica(request):
    pagina="Basilica"
    language = request.LANGUAGE_CODE

    logger.debug(f"----------Contenuto della sessione: {request.session.items()}")
    #paragrafo=_("paragrafo")
    return render(request, 'itinerarioPirandelliano/Basilica.html',{"pagina":pagina, "lang_name":language})

def Cattedrale(request):
    pagina="Cattedrale"
    language = request.LANGUAGE_CODE

    logger.debug(f"----------Contenuto della sessione: {request.session.items()}")
    #paragrafo=_("paragrafo")
    return render(request, 'itinerarioPirandelliano/Cattedrale.html',{"pagina":pagina, "lang_name":language})

def Pirandello(request):
    pagina="Pirandello"
    language = request.LANGUAGE_CODE


    logger.debug(f"----------Contenuto della sessione: {request.session.items()}")
    #paragrafo=_("paragrafo")
    return render(request, 'itinerarioPirandelliano/Pirandello.html',{"pagina":pagina, "lang_name":language})

def VialeVittoria(request):
    pagina="VialeVittoria"
    language = request.LANGUAGE_CODE


    logger.debug(f"----------Contenuto della sessione: {request.session.items()}")
    #paragrafo=_("paragrafo")
    return render(request, 'itinerarioPirandelliano/VialeVittoria.html',{"pagina":pagina, "lang_name":language})


def CasaRavanusella(request):
    pagina="CasaRavanusella"
    language = request.LANGUAGE_CODE


    logger.debug(f"----------Contenuto della sessione: {request.session.items()}")
    #paragrafo=_("paragrafo")
    return render(request, 'itinerarioPirandelliano/CasaRavanusella.html',{"pagina":pagina, "lang_name":language})







def set_language(request):
    language = request.GET.get('language', None)
    pagina = request.GET.get('pagina', None)
    logger.debug(f"Variabile 'pagina' ricevuta: {pagina}")
    

    if language and language in [code for code, _ in settings.LANGUAGES]:
        # Imposta la lingua della sessione di Django
        activate(language)

    # Crea un URL con la lingua incorporata e usa reverse per ottenere il percorso completo
    language_url = reverse(pagina)
    logger.debug(f"{language_url}")
    
    return redirect(language_url)

#def set_language(request):
    language = request.GET.get('language', None)
    stringa = request.POST.get('pagina')
    logger.debug(f"{stringa}")

    if language and language in [code for code, _ in settings.LANGUAGES]:
        # Imposta la lingua della sessione di Django
        activate(language)

    # Verifica se 'pagina' è un valore valido
    if stringa is not None:
        try:
            # Tenta di ottenere l'URL usando il valore di 'pagina'
            language_url = reverse(stringa)
            logger.debug(f"{language_url}")
            logger.debug(f"fattooo")
            return redirect(language_url)
        except:
            # Gestisci eventuali eccezioni (ad esempio, URL non trovato)
            logger.error("Errore nella generazione dell'URL per la pagina specificata.")
    
    # Gestisci il caso in cui 'pagina' non sia specificato o non valido
    logger.error("Valore 'pagina' non valido o non specificato.")
    # Puoi reindirizzare a una pagina predefinita o fare qualsiasi altra azione necessaria

    return redirect('home')


