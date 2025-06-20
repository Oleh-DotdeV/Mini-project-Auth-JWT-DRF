# import django_filters
# from .models import Note
#
# class NoteFilter(django_filters.FilterSet):
#     created_at = django_filters.DateFilter(field_name='created_at', lookup_expr='date')
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     tags = django_filters.CharFilter(method='filter_by_tag_name')
#
#     class Meta:
#         model = Note
#         fields = ['created_at', 'title', 'tags']
#
#     def filter_by_tag_name(self, queryset, name, value):
#         return queryset.filter(tags__name__icontains=value)