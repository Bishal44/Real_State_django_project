from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from .models import Listing

def index(request):
    listing=Listing.objects.order_by('-list_date').filter(is_published=True)

    #for paginator case
    paginator=Paginator(listing,3)
    page=request.GET.get('page')
    page_listed=paginator.get_page(page)

    context={
        'listings':page_listed
        #'listings':listing if no paginator there
    }
    return render(request,'listings/listings.html',context)
def listing(request,listing_id):
    return render(request,'listings/listing.html')
def search(request):
    return render(request,'listings/search.html')
