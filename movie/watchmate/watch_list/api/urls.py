from django.urls import path, include

from ..api import views

urlpatterns = [
    path('list/', views.movie_list, name='movie_list'),
    path('list/<int:pk>', views.movie_detail, name='movie_detail'),
]
