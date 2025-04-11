from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .api import serializers
from . import models


# Create your tests here.


class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='password123')
        self.token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream_platform = models.StreamPlatform.objects.create(name="Netflix", about="#1 streaming platform",
                                                                    website="https://netflix.com", )

    def test_streamplatform_create(self):
        data = {
            "name": "Netflix",
            "about": "#1 streaming platform",
            "website": "https://netflix.com",
        }
        response = self.client.post(reverse('platforms-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('platforms-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_individual(self):
        response = self.client.get(reverse('platform-detail', args=(self.stream_platform.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WatchListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='password123')
        self.token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream_platform = models.StreamPlatform.objects.create(name="Netflix", about="#1 streaming platform",
                                                                    website="https://netflix.com")

        self.watch_list = models.WatchList.objects.create(title="Example Title", description="Example Description",
                                                          active=True, platform=self.stream_platform)

    def test_watchlist_create(self):
        data = {
            "title": "Example Title",
            "description": "Example Description",
            "active": True,
            "platform": self.stream_platform,
        }
        response = self.client.post(reverse('movie_list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_individual(self):
        response = self.client.get(reverse('movie_detail', args=(self.watch_list.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, 'Example Title')


class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='password123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream_platform = models.StreamPlatform.objects.create(name="Netflix", about="#1 streaming platform",
                                                                    website="https://netflix.com")

        self.watch_list = models.WatchList.objects.create(title="Example Title", description="Example Description",
                                                          active=True, platform=self.stream_platform)

        self.watch_list2 = models.WatchList.objects.create(title="Example Title 2", description="Example Description 2",
                                                          active=True, platform=self.stream_platform)

        self.review = models.Review.objects.create(reviewer=self.user, rating=5, description="Review Description",
                                                   active=True, watchlist=self.watch_list2)

    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Review Description",
            "watchlist": self.watch_list,
            "active": True,
        }

        response = self.client.post(reverse('review-create', args=(self.watch_list.pk,)), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)
        self.assertEqual(models.Review.objects.get().rating, 5)

        response = self.client.post(reverse('review-create', args=(self.watch_list.pk,)), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_create_unauthenticated(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Review Description",
            "watchlist": self.watch_list,
            "active": True,
        }

        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create', args=(self.watch_list.pk,)), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def tset_review_update(self):
        data = {
            "review_user": self.user,
            "rating": 4,
            "description": "Review Description - Updated",
            "watchlist": self.watch_list,
            "active": False,
        }

        response = self.client.put(reverse('review-detail', args=(self.review.pk,)), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=self.watch_list.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_detail(self):
        response = self.client.get(reverse('review-detail', args=self.review.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
