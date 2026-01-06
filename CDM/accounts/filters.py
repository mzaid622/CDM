import django_filters
from .models import Order


class OrderFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter("date_created", lookup_expr="gte")
    end_date = django_filters.DateFilter("date_created", lookup_expr="lte")
    note = django_filters.CharFilter(field_name="note", lookup_expr="icontains")

    class Meta:
        model = Order
        fields = "__all__"
        exclude = ["customer", "date_created"]
