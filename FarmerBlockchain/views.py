from django.shortcuts import render

from sellers.forms import SellerUserRegistrationForm
from buyers.forms import BuyerUserRegistrationForm


def index(request):
    return render(request,"index.html",{})


def logout(request):
    return render(request, 'index.html', {})

def SellerLogin(request):
    return render(request, 'SellerLogin.html', {})


def BuyerLogin(request):
    return render(request, 'BuyerLogin.html', {})

def AdminLogin(request):
    return render(request, 'AdminLogin.html', {})


def SellerRegister(request):
    form = SellerUserRegistrationForm()
    return render(request, 'SellerUserRegistrations.html', {'form': form})


def BuyerRegister(request):
    form = BuyerUserRegistrationForm()
    return render(request, 'BuyerUserRegistrations.html', {'form': form})
