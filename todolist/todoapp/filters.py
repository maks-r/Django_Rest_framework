import django_filters
from django_filters import rest_framework as filters
from .models import ToDo


class TodoFilter(filters.FilterSet):
    project = django_filters.NumberFilter()
    start_date = filters.DateTimeFilter(field_name="start_date", lookup_expr='gt')
    expiration_date = filters.DateTimeFilter(field_name="expiration_date", lookup_expr='lt')

    class Meta:
        model = ToDo
        fields = ['project', 'start_date', 'expiration_date']
