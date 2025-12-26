from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    total_order_delivared = orders.filter(status="Delivered").count()
    total_order_pending = orders.filter(status="Pending").count()

    context = {"customers": customers, "orders": orders, "total_orders": total_orders,"total_order_delivared":total_order_delivared,"total_order_pending":total_order_pending}
    return render(
        request,
        "accounts/home.html",
        context,
    )


def products(request):
    product = Product.objects.all()

    return render(request, "accounts/products.html", {"product": product})


def customer(request,pk_id):
    cust = Customer.objects.get(id=pk_id)

    order=cust.order_set.all()

    order_count = order.count()

    context = {"cust":cust,"order":order,"order_count":order_count}
    return render(request, "accounts/customer.html",context)
