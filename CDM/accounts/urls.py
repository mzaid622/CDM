from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("customer/<str:pk_id>", views.customer, name="customer"),
    path("create_order/<str:pk_id>", views.createorder, name="create_order"),
    path("edit_order/<str:pk_id>",views.editorder,name="edit_order"),
    path("delete_order/<str:pk_id>",views.deleteorder,name="delete_order"),
]

