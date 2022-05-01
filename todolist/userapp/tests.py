import random

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate, APITestCase
from .views import UserModelViewSet
from .models import User
from django.contrib.auth.models import User
from mixer.backend.django import mixer


class TestUserApi(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='Maks', password='pbkdf2_sha256$260000$Dhc0fuOXs5DG8IRHyOrAd4$dk7jHzKvShxgVaL6y2TSnLOjhuziKqnHLRORKIcGjWI=')


    def test_get_user(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = UserModelViewSet.as_view({'get': 'user'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_user_1(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        force_authenticate(request, self.user)
        view = UserModelViewSet.as_view({'get': 'user'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class TestUserApiClient(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='maks-r', password='adminadmin6916')
        self.author = mixer.blend(User, age=mixer.sequence(lambda c: random.random() * 100))

    def test_get_user(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_user_1(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_user_2(self):
        self.client.login(username='maks-r', password='adminadmin6916')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.client.logout()
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_user(self):
        self.client.login(username='maks-r', password='adminadmin6916')
        response = self.client.post('/api/users/', data={
            'first_name': 'Максим'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(pk=response.data.get('id'))
        self.assertEqual(user.first_name, 'Максим')