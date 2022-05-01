import random

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate, APITestCase
from .views import ProjectViewSet
from .models import Project, ToDo
from userapp.models import User
from mixer.backend.django import mixer


class TestProjectApi(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='Maks',
                                                  password='pbkdf2_sha256$260000$Dhc0fuOXs5DG8IRHyOrAd4$dk7jHzKvShxgVaL6y2TSnLOjhuziKqnHLRORKIcGjWI=')

    def test_get_project(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects')
        view = ProjectViewSet.as_view({'get': 'project'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_project_1(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects')
        force_authenticate(request, self.user)
        view = ProjectViewSet.as_view({'get': 'project'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class TestProjectApiClient(APITestCase):

    def setUp(self) -> None:
        self.project = mixer.blend(Project, name=mixer.sequence(lambda c: random.random() * 100))
        self.todo = mixer.blend(ToDo, project=1)

    def test_get_project(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_project_1(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_list_todo(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        print(response.data)
