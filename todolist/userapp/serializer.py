from .models import User
from rest_framework.serializers import ModelSerializer


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserModelSerializerV2(ModelSerializer):
    class Meta:
        model = User
        fields = ['is_superuser', 'is_staff']

