from django.urls import path, include

from ..api import views

urlpatterns = [
    path('list/', views.MovieListApiView.as_view(), name='movie_list'),
    path('list/<int:pk>', views.MovieDetailApiView.as_view(), name='movie_detail'),
]
