from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import UserModelSerializer
from rest_framework import mixins, viewsets


class UserModelViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
