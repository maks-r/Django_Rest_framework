from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserModelViewSet
from todoapp.views import ProjectViewSet, ToDoViewSet

app_name = 'userapp'

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectViewSet)
router.register('todos', ToDoViewSet)


urlpatterns = [
    path('', include(router.urls))
]
