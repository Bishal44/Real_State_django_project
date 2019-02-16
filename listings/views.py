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

    query_list=Listing.objects.order_by('-list_date')
    #keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:      #to check empty keyword
            query_list=query_list.filter(description__icontains=keywords) #to search in description

    #city
    if 'city' in request.GET:
        city=request.GET['city']
        if city:      #to check empty keyword
            query_list=query_list.filter(city__iexact=city) #for exjact matching

  # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:  # to check empty keyword
             query_list = query_list.filter(state__iexact=state)  # for exjact matching
# bedroom
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']#in fornt end search for name attribute of select tag
        if bedrooms:  # to check empty keyword
            query_list = query_list.filter(beadrooms__lte=bedrooms)  # for less than equal to matching
 # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:  # to check empty keyword
             query_list = query_list.filter(price__lte=price)  # for less than equal to matching

    context={
        'state_choices': state_choices,
        'bed_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings':query_list
    }
    return render(request,'listings/search.html',context)
