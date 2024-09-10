from django.shortcuts import render,HttpResponse
from django.contrib import messages
from sellers.models import SellerUserRegistrationModel
from buyers.models import BuyerUserRegistrationModel
from buyers.models import BuyerCropCartModels,BlockChainTransactionModel

# Create your views here.

def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')
        elif usrid == 'Admin' and pswd == 'Admin':
            return render(request, 'admins/AdminHome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})


def AdminHome(request):
    return render(request, 'admins/AdminHome.html')


def ViewSellersRegisteredUsers(request):
    data = SellerUserRegistrationModel.objects.all()
    return render(request, 'admins/SellersRegisteredUsers.html', {'data': data})


def AdminActivaSellersUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        SellerUserRegistrationModel.objects.filter(id=id).update(status=status)
        data = SellerUserRegistrationModel.objects.all()
        return render(request, 'admins/SellersRegisteredUsers.html', {'data': data})


def ViewBuyersRegisteredUsers(request):
    data = BuyerUserRegistrationModel.objects.all()
    return render(request, 'admins/BuyersRegisteredUsers.html', {'data': data})


def AdminActivaBuyerssUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        BuyerUserRegistrationModel.objects.filter(id=id).update(status=status)
        data = BuyerUserRegistrationModel.objects.all()
        return render(request, 'admins/BuyersRegisteredUsers.html', {'data': data})

def AdminViewAllPurchased(request):
    data = BuyerCropCartModels.objects.filter(status='purchased')
    return render(request,'admins/AdminViewAllPurchased.html',{'data':data})

def AdminViewAllBlockChainData(request):
    data = BlockChainTransactionModel.objects.all()
    return render(request, 'admins/AdminViewAllBlockChainTransaction.html', {'data': data})