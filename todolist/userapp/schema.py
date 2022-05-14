import graphene
from graphene_django import DjangoObjectType
from .models import User
from todoapp.models import Project, ToDo


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info):
        return User.objects.all()

    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(self, info):
        return Project.objects.all()

    all_todos = graphene.List(ToDoType)

    def resolve_all_todos(self, info):
        return ToDo.objects.all()



schema = graphene.Schema(query=Query)

# КАК ТО ВСЕ ЛЕГКО ПОЛУЧИЛОСЬ, ЕСЛИ Я ПРАВИЛЬНО ПОНЯЛ ДОМАШНЕЕ ЗАДАНИЕ.
# В GRAPHQL
# {
#   allTodos
#   {
#     text
#     project
#     {
#       name
#       users{
#         firstName
#       }
#     }
#   }
# }