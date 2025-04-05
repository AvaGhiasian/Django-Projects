from django.urls import path

from ..api import views

urlpatterns = [
    path('list/', views.WatchListAPIView.as_view(), name='movie_list'),
    path('list/<int:pk>/', views.WatchListDetailAPIView.as_view(), name='movie_detail'),
    path('platform/', views.StreamPlatformAPIView.as_view(), name='platform'),
    path('platform/<int:pk>/', views.StreamPlatformDetailAPIView.as_view(), name='platform_detail'),
    path('<int:pk>/reviews/', views.ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('<int:pk>/review-create/', views.ReviewCreateView.as_view(), name='review_create'),
]
