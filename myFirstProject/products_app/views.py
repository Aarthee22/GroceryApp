from django.shortcuts import render,redirect
from .models import OrderList
from django.contrib import messages 
from groceries_new import views as groceries_view
from groceries_new import models as groceries_model
from django.core.mail import send_mail
from django.conf import settings



def product_list(request):
    products = {"dairy": ["milk","yougurt","cheese","butter"],
                "beverages":["soda","juice"],
                "vegetables":["carrots","onion","tomato"],
                "fruits":["apples","bananas","grapes"]}
    return render(request,"product_list.html",products)
# Create your views here.

def order(request):
    if request.method=="POST":
        prod_list=request.POST.getlist('products')
        prod_str=",".join(prod_list)
        order_data=OrderList(wholeList=prod_str,username=groceries_view.usrnme)
        order_data.save()
        user_data=groceries_model.RegisteredUser.objects.get(name=groceries_view.usrnme)
        recipient_list=[user_data.emailid, ]
        send_mail("Order from Loony Basket",
                 "Hi, \n\n Below are the products you have ordered from Loony Basket. \n\n {}".format(prod_str),
                  settings.EMAIL_HOST_USER,
                  recipient_list
        )
        messages.success(request,"Order has been placed successfully and an email has been sent")
        return render(request,"ordersuccess.html")
    else:
        return render(request, "product_list.html")