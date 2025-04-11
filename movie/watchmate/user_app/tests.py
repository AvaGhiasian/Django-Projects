from http.client import responses

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


# Create your tests here.

class RegisterTestCase(APITestCase):
    def test_register(self):
        """ for  testing:
        get data,
        send post request,
        get response and check response is current or not """

        data = {
            'username': 'testcase',
            'email': 'testcase@example.com',
            'password': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(reverse('register'), data)  # sends a post request with data to that url
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # if we 201 means that we have created the user


class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='password123')

    def test_login(self):
        data = {
            "username": "example",
            "password": "password123",
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        """ we need to access token and pass it for logging out """
        self.token = Token.objects.get(user__username="example")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
