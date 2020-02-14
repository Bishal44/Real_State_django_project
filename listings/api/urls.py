"""
Real_State_django_project
Created by Bishal on 14 Feb 2020
"""
from django.urls import path

from listings.api import views

urlpatterns = [
    path("<int:listing_id>", views.api_detail_listing, name="listing_api"),
]