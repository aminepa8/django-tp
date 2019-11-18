from django.urls import path
#from django.conf.urls import url
from  . import views
urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('', views.index,{'pagename':''}, name='home'),
    path('<str:pagename>', views.index, name='index'),
    
]
