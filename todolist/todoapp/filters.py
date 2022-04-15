import django_filters
from django_filters import rest_framework as filters
from .models import ToDo


# class ProductFilter(django_filters.FilterSet):
#     price = django_filters.NumberFilter()
#     price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
#     price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
#
#     release_year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
#     release_year__gt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__gt')
#     release_year__lt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__lt')
#
#     manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')
#
#     class Meta:
#         model = Product
#         fields = ['price', 'release_date', 'manufacturer']


class TodoFilter(filters.FilterSet):
    project = django_filters.NumberFilter()
    start_date = filters.DateTimeFilter(field_name="start_date", lookup_expr='gt')
    expiration_date = filters.DateTimeFilter(field_name="expiration_date", lookup_expr='lt')

    class Meta:
        model = ToDo
        fields = ['project', 'start_date', 'expiration_date']
