from django.urls import path

from ..api import views

urlpatterns = [
    path('list/', views.WatchListAPIView.as_view(), name='movie_list'),
    path('list/<int:pk>/', views.WatchListDetailAPIView.as_view(), name='movie_detail'),
    path('platforms/', views.StreamPlatformAPIView.as_view(), name='platform'),
    path('platforms/<int:pk>/', views.StreamPlatformDetailAPIView.as_view(), name='platform-detail'),
    path('<int:pk>/reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('<int:pk>/review-create/', views.ReviewCreateView.as_view(), name='review-create'),
    path('reviews/', views.UserReviewView.as_view(), name='user-review-detail'),
]
