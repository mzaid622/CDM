from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import *
from .form import OrderForm

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


def createorder(request):

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = OrderForm()

    context = {"form":form}
    return render(request,"accounts/order_form.html",context)


def editorder(request,pk_id):
    order = Order.objects.get(id=pk_id)

    if request.method == "POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = OrderForm(instance = order)

    context = {"form":form}
    return render(request,"accounts/order_form.html",context)


def deleteorder(request,pk_id):
    item = Order.objects.get(id=pk_id)
    item_n=item.product

    if request.method == "POST":
        item.delete()
        return redirect("/")


    context = {"item":item_n}
    return render(request,"accounts/delete_form.html",context)