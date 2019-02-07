from django.shortcuts import render
#from django.http import HttpResponse #only for html from here
from listings.models import Listing
from realtors.models import Realtor
def index(request):

    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3] #for recent listing in index page
    contex ={
        'listings':listings
    }
    return render(request,'pages/index.html',contex)
def about(request):
    #get all realtor
    realtors=Realtor.objects.order_by('-hire_date')

    #get seller of month (mvp checked)
    mvp_realtor=Realtor.objects.all().filter(is_mvp=True)

    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtor,

    }
    return render(request,'pages/about.html',context)
