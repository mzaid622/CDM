from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
# from django.http import HttpResponse
from .models import *
from .form import OrderForm
from .filters import OrderFilter

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

    my_filter = OrderFilter(request.GET,queryset=order)
    order = my_filter.qs
    order_count = order.count()

    context = {"cust":cust,"order":order,"order_count":order_count,"my_filter":my_filter}
    return render(request, "accounts/customer.html",context)


def createorder(request,pk_id):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)

    customer = Customer.objects.get(id=pk_id)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == "POST":
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("/")

    context = {"formset":formset}
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