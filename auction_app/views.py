from decimal import Decimal

from django.contrib.auth import logout
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import product
from django.contrib.auth.decorators import login_required
from .models import Bid
import logging


def home(request):
    return render(request, 'index.html')


@login_required()
def products(request):
    items = product.objects.all()
    return render(request, "products.html", {'result': items})

@login_required()
def productdetail(request, product_id):
    # item=product.objects.get(id=product_id)
    Product= get_object_or_404(product, pk=product_id)
    return render(request,'product-detail.html',{'product':Product})



def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken.")
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.error(request, "username already taken.")

            else:
                user = User.objects.create_user(email=email, username=username, password=password)

                user.save()

        else:
            messages.info(request, "password not matching")
            return redirect('register')

        return redirect('login')
    return render(request, 'sign-up.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('products')

        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "sign-in.html")



def my_logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def save_bid(request):
    if request.method == 'POST':
        product_id = request.POST.get('productId')
        mobile = request.POST.get('inputMobile')
        bid_amount = request.POST.get('inputPrice')

        # Check if bid_amount is not None and not empty
        if bid_amount:
            # Convert bid_amount to Decimal
            bid_amount = Decimal(bid_amount)

            # Save bid to the database
            bid = Bid.objects.create(
                user=request.user,
                product_id=product_id,
                bid_amount=bid_amount,
                mobile=mobile,
            )
            bid.save()

            return redirect('success')
        else:
            return render(request, 'bid_error.html', {'error_message': 'Bid amount is required.'})
    else:
        return redirect('/')




def success(request):
    return render(request,'Congratulation.html')