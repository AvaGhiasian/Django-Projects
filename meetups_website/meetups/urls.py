from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="all-meetups"),
    path("<slug:meetup_slug>/success", views.confirm_registration, name="confirm-registration"),
    path("<slug:meetup_slug>",  views.meetup_details, name="meetup-detail") # domain.com/meetups/<dynamic-pat-segment>
] 
