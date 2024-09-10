from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import SellerUserRegistrationForm
from .models import SellerUserRegistrationModel, FarmersCropsModels
from django.core.files.storage import FileSystemStorage
from buyers.models import BuyerCropCartModels, BuyerTransactionModels

# Create your views here.
def SellerUserRegisterActions(request):
    if request.method == 'POST':
        form = SellerUserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = SellerUserRegistrationForm()
            return render(request, 'SellerUserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = SellerUserRegistrationForm()
    return render(request, 'SellerUserRegistrations.html', {'form': form})
def SellerUserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = SellerUserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'sellers/SellerUserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'SellerLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'SellerLogin.html', {})
def SellerUserHome(request):
    return render(request, 'sellers/SellerUserHome.html', {})

def SellerAddItemsForm(request):
    return render(request, 'sellers/SellerAddItems.html',{})

def SellerAddItemsAction(request):
    if request.method=='POST':
        cropname = request.POST.get('cropname')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image_file = request.FILES['file']
        Date_time = request.POST.get('date')
        # Date_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M:%S'], widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S'))
        # let's check if it is a csv file
        if not image_file.name.endswith('.jpg'):
            messages.error(request, 'THIS IS NOT A JPG  FILE')

        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        detect_filename = fs.save(image_file.name, image_file)
        uploaded_file_url = fs.url(filename)
        loginid = request.session['loginid']
        email = request.session['email']
        price=int(price)
        rate = int(price*75/100)
        rate=float(rate)
        FarmersCropsModels.objects.create(sellername=loginid, selleremail=email, cropname=cropname,price=price, description=description,file=uploaded_file_url,cdate= Date_time, rate= rate)
        messages.success(request, 'Ticket Data Addedd Success')
        return render(request, 'sellers/SellerAddItems.html', {})

def SellersCommodities(request):
    loginid = request.session['loginid']
    data = FarmersCropsModels.objects.filter(sellername=loginid)
    return render(request, 'sellers/SellersCommoditiesData.html',{'data':data})

def SellerUpdateProducts(request):
    cropid = request.GET.get('cropid')
    data = FarmersCropsModels.objects.get(id=cropid)
    return render(request, 'sellers/CropsUpdatesbySeller.html', {'data': data})

    return HttpResponse("Update products Working Success")

def SellerDeleteProducts(request):
    cropid = request.GET.get('cropid')
    FarmersCropsModels.objects.filter(id=cropid).delete()
    loginid = request.session['loginid']
    data = FarmersCropsModels.objects.filter(sellername=loginid)
    return render(request, 'sellers/SellersCommoditiesData.html', {'data': data})


def SellerCropUpdateAction(request):
    #MyModel.objects.filter(pk=some_value).update(field1='some value')
    cropname = request.POST.get('cropname')
    price = request.POST.get('price')
    cropid = request.POST.get('cropid')
    description = request.POST.get('description')
    image_file = request.FILES['file']
    # let's check if it is a csv file
    if not image_file.name.endswith('.jpg'):
        messages.error(request, 'THIS IS NOT A JPG  FILE')

    fs = FileSystemStorage()
    filename = fs.save(image_file.name, image_file)
    detect_filename = fs.save(image_file.name, image_file)
    uploaded_file_url = fs.url(filename)
    rate= price*75/100
    FarmersCropsModels.objects.filter(id=cropid).update(cropname=cropname, price=price, description=description, file=uploaded_file_url, rate=rate)
    loginid = request.session['loginid']
    data = FarmersCropsModels.objects.filter(sellername=loginid)
    return render(request, 'sellers/SellersCommoditiesData.html', {'data': data})

def SellerViewCarts(request):
    sellername = request.session['loginid']
    data = BuyerCropCartModels.objects.filter(sellername=sellername)
    print(data)

    # re_amount = BuyerCropCartModels.objects.values()
    # # ratings=dict(ratings)
    # print(type(re_amount))
    # # ratings.objects.values()
    # print(re_amount)
    #
    # # ratings=ratings['userrating']
    # kamount=[]
    # for k in re_amount:
    #     m = dict(k)
    #     # print(m)
    #     for i, j in m.items():
    #         print(i, j)
    #         if j == sellername:
    #
    #             re_amount = k['price']
    #             print(re_amount)
    #             amount = re_amount * 75/100
    #             amount=int(amount)
    #             kamount.append(amount)
    return render(request,'sellers/SellersViewCart.html',{'data':data})
