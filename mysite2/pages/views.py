from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
# Create your views here.
from pages.models import Page
from .forms import ContactForm

def contact(request):
    submitted = False
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.isvalid():
            cd=form.cleaned_data
            # assert False
            return HttpResponseRedirect('/contact/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
            pass
    return render(request,'pages/contact.html',{'form':form,page_list: Page.objects.all(),'submitted' :submitted})

def index(request, pagename):
    pagename = '/' + pagename
    pg       = Page.objects.get(permalink=pagename)
    context  = {
        'title'        : pg.title,
        'content'      : pg.bodytext,
        'last_updated' : pg.update_date,
        'page_list'    :Page.objects.all(),
    }
    #assert False
    return render(request, 'pages/page.html', context)
