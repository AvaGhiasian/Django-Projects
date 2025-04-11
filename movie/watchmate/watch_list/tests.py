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
