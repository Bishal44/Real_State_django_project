from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Listing
from .choices import price_choices,state_choices,bedroom_choices

def index(request):
    listing=Listing.objects.order_by('-list_date').filter(is_published=True)

    #for paginator case
    paginator=Paginator(listing,5)
    page=request.GET.get('page')
    page_listed=paginator.get_page(page)

    context={
        'listings':page_listed,
        #'listings':listing if no paginator there

    }
    return render(request,'listings/listings.html',context)
def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)

    context={
        'listing':listing
    }
    return render(request,'listings/listing.html',context)
def search(request):
    context={
        'state_choices': state_choices,
        'bed_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request,'listings/search.html',context)
