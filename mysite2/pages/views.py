from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from pages.models import Page


def index(request, pagename):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    #return HttpResponse(""" <h1>Bienvenue au site de GLASSRI !</h1> <p>JARID Chaimae !</p> """)
    #return render(request, "base.html")
    #return render(request, "pages/page.html")
    pagename = '/' + pagename
    pg       = Page.objects.get(permalink=pagename)
    context  = {
        'title'        : pg.title,
        'content'      : pg.bodytext,
        'last_updated' : pg.update_date,
    }
    #assert False
    return render(request, 'pages/page.html', context)
