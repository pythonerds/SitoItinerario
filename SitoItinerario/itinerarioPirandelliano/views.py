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

def secondaPagina(request):
    pagina="home"


    logger.debug(f"----------Contenuto della sessione: {request.session.items()}")
    #paragrafo=_("paragrafo")
    return render(request, 'itinerarioPirandelliano/secondaPagina.html',{"pagina":pagina})






def set_language(request):
    language = request.GET.get('language', None)
    

    if language and language in [code for code, _ in settings.LANGUAGES]:
        # Imposta la lingua della sessione di Django
        activate(language)

    # Crea un URL con la lingua incorporata e usa reverse per ottenere il percorso completo
    language_url = reverse('home')
    logger.debug(f"{language_url}")
    
    return redirect(language_url)


