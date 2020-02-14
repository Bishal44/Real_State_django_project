"""
Real_State_django_project
Created by Bishal on 14 Feb 2020
"""
from rest_framework import serializers
from listings.models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['realtor', 'title', 'address','city','state','zipcode','description','price','beadrooms','bathrooms','garage',
                  'sqft','lot_size','photo_main','is_published','list_date']