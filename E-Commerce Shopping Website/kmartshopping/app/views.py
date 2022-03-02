from ast import Pass
from tkinter import N
from unicodedata import category, name
from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CutomerRegistrationForm, CustomerProfileForm
from django.contrib import messages

# def home(request):
#  return render(request, 'app/home.html')


class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'app/home.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles, 'laptops': laptops})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})


def add_to_cart(request):
    return render(request, 'app/addtocart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')


def mobile(request, data=None):
    lst = ['Redmi', 'Samsung', 'OPPO', 'Vivo', 'realme']
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data in lst:
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__lt=13000)
    elif data == 'above':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__gt=13000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})


def laptop(request, data=None):
    lst = ['Acer', 'ASUS', 'Lenovo', 'HP', 'AVITA', 'Redmi', 'Dell']
    if data == None:
        laptops = Product.objects.filter(category='L')
    elif data in lst:
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below':
        laptops = Product.objects.filter(
            category='L').filter(discounted_price__lt=40000)
    elif data == 'above':
        laptops = Product.objects.filter(
            category='L').filter(discounted_price__gt=40000)

    return render(request, "app/laptop.html", {'laptops': laptops})


def topWear(request, data=None):
    if data == None:
        topwears = Product.objects.filter(category='TW')
    elif data == 'below':
        topwears = Product.objects.filter(
            category='TW').filter(discounted_price__lt=500)
    elif data == 'above':
        topwears = Product.objects.filter(
            category='TW').filter(discounted_price__gt=500)

    return render(request, 'app/topwear.html', {'topwears': topwears})


def bottomWear(request, data=None):
    if data == None:
        bottomwears = Product.objects.filter(category='BW')
    elif data == 'below':
        bottomwears = Product.objects.filter(
            category='BW').filter(discounted_price__lt=800)
    elif data == 'above':
        bottomwears = Product.objects.filter(
            category='BW').filter(discounted_price__gt=800)
    return render(request, 'app/bottomwear.html', {'bottomwears': bottomwears})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CutomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CutomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})


def checkout(request):
    return render(request, 'app/checkout.html')


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality,
                           city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(
                request, 'Congratulations!! Profile Updated Successfully')
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})
