from django.urls import path, include

from ..api import views

urlpatterns = [
    path('list/', views.WatchListAPIView.as_view(), name='movie_list'),
    path('list/<int:pk>', views.WatchListDetailAPIView.as_view(), name='movie_detail'),
    path('platform/', views.StreamPlatformAPIView.as_view(), name='platform'),
    path('platform/<int:pk>/', views.StreamPlatformDetailAPIView.as_view(), name='platform_detail'),
]
