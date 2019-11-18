from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect
#-------------------------------------------------------
from django.core.mail import send_mail, get_connection
#-------------------------------------------------------
# Create your views here.
from pages.models import Page
from .forms import ContactForm

def contact(request):
    submitted = False
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            # assert False 
#-------------------------------------------------------
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(cd['subject'],cd['message'],cd.get('email','noreply@gmail.com'),
                        ['lpglassri@gmail.com'],connection=con)
#-------------------------------------------------------
            return HttpResponseRedirect('/contact?submitted=True')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
            pass
    return render(request,'pages/contact.html',{'form':form,'page_list': Page.objects.all(),'submitted' :submitted})

def index(request, pagename):
    pagename = '/' + pagename
    #pg       = Page.objects.get(permalink=pagename)
    pg = get_object_or_404(Page, permalink=pagename)
    context  = {
        'title'        : pg.title,
        'content'      : pg.bodytext,
        'last_updated' : pg.update_date,
        'page_list'    :Page.objects.all(),
    }
    #assert False
    return render(request, 'pages/page.html', context)
