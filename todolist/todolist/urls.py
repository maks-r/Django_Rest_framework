from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from userapp.views import UserModelViewSet
from todoapp.views import ProjectViewSet, ToDoViewSet
from rest_framework.authtoken import views
from userapp.views import *
from todoapp.views import *
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, Contact, License
from graphene_django.views import GraphQLView


schema_view = get_schema_view(
    Info(
        title='Userapp',
        default_version='1.0',
        description='description',
        contact=Contact(email='test@test.com'),
        license=License(name='MIT')
    ),
    public=True,
    permission_classes=(AllowAny, )
)


router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectViewSet)
router.register('todos', ToDoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    #path('api/', include(userapp.urls)),
    # path('api/', include('userapp.urls', namespace='1.0')),
    # path('api/v1/', include('userapp.urls', namespace='1.0')),
    # path('api/v2/', include('userapp.urls', namespace='1.1')),
    path('swagger/', schema_view.with_ui()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    path('api-auth-token/', views.obtain_auth_token),
]