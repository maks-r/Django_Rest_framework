import django_filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from .filters import TodoFilter
from .serializer import ProjectSerializer, ToDoSerializer
from .models import Project, ToDo


# class ProjectOffsetPagination(LimitOffsetPagination):
#     default_limit = 10


class ProjectViewSet(ModelViewSet):
    # pagination_class = ProjectOffsetPagination
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name:
            return Project.objects.filter(name__contains=name)
        return Project.objects.all()


# class ToDoOffsetPagination(LimitOffsetPagination):
#     default_limit = 20


class ToDoViewSet(ModelViewSet):
    # pagination_class = ToDoOffsetPagination
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = TodoFilter

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()


