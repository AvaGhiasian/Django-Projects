from django.urls import path

from . import views

urlpatterns = [
    path("meetups", views.index, name="all-meetups"), # domain.com/meetups
    path("meetups/<slug:meetup_slug>",  views.meetup_details, name="meetup-detail") # domain.com/meetups/<dynamic-pat-segment>
] 
