"""
Real_State_django_project
Created by Bishal on 14 Feb 2020
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from listings.api.serializers import ListingSerializer
from listings.models import Listing
#Listing.objects.get(listing_id=listing_id)
@api_view(['GET',])
def api_detail_listing(request,listing_id):
    try:
        listing = get_object_or_404(Listing, pk=listing_id)
    except Listing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ListingSerializer(listing)
    return Response(serializer.data)
