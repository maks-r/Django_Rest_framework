from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import UserModelSerializer, UserModelSerializerV2
from rest_framework import mixins, viewsets


class UserModelViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    # serializer_class = UserModelSerializer
    queryset = User.objects.all()

    vers = {
        '1.1': UserModelSerializerV2
    }

    def get_serializer_class(self):
        return self.vers.get(self.request.version, UserModelSerializer)
