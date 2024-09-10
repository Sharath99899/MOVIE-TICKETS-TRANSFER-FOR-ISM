"""FarmerBlockchain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FarmerBlockchain import views as mainView
from sellers import views as seller
from admins import views as admins
from buyers import views as buyer
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView.index, name='index'),
    path("index/", mainView.index, name="index"),
    path("logout/", mainView.logout, name="logout"),
    path("SellerLogin/", mainView.SellerLogin, name="SellerLogin"),
    path("BuyerLogin/", mainView.BuyerLogin, name="BuyerLogin"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path("SellerRegister/", mainView.SellerRegister, name="SellerRegister"),
    path("BuyerRegister/", mainView.BuyerRegister, name="BuyerRegister"),

    ### Seller Side Views
    path("SellerUserRegisterActions/", seller.SellerUserRegisterActions, name="SellerUserRegisterActions"),
    path("SellerUserLoginCheck/", seller.SellerUserLoginCheck, name="SellerUserLoginCheck"),
    path("SellerUserHome/", seller.SellerUserHome, name="SellerUserHome"),
    path("SellerAddItemsForm/", seller.SellerAddItemsForm, name="SellerAddItemsForm"),
    path("SellerAddItemsAction/", seller.SellerAddItemsAction, name="SellerAddItemsAction"),
    path("SellersCommodities/", seller.SellersCommodities, name="SellersCommodities"),
    path("SellerUpdateProducts/", seller.SellerUpdateProducts, name="SellerUpdateProducts"),
    path("SellerDeleteProducts/", seller.SellerDeleteProducts, name="SellerDeleteProducts"),
    path("SellerCropUpdateAction/", seller.SellerCropUpdateAction, name="SellerCropUpdateAction"),
    path("SellerViewCarts/", seller.SellerViewCarts, name="SellerViewCarts"),


    ### Buyer Side Views
    path("BuyerUserRegisterActions/", buyer.BuyerUserRegisterActions, name="BuyerUserRegisterActions"),
    path("BuyerUserLoginCheck/", buyer.BuyerUserLoginCheck, name="BuyerUserLoginCheck"),
    path("BuyerUserHome/", buyer.BuyerUserHome, name="BuyerUserHome"),
    path("BuyerSearchProductsForm/", buyer.BuyerSearchProductsForm, name="BuyerSearchProductsForm"),
    path("BuyerSearchCropsAction/", buyer.BuyerSearchCropsAction, name="BuyerSearchCropsAction"),
    path("BuyerAddCropsToCart/", buyer.BuyerAddCropsToCart, name="BuyerAddCropsToCart"),
    path("BuyyerCheckCartData/", buyer.BuyyerCheckCartData, name="BuyyerCheckCartData"),
    path("BuyerDeleteanItemfromCart/", buyer.BuyerDeleteanItemfromCart, name="BuyerDeleteanItemfromCart"),
    path("startBlockChainProcess/", buyer.startBlockChainProcess, name="startBlockChainProcess"),
    path('BuyerTotalAmountCheckOut/', buyer.BuyerTotalAmountCheckOut, name='BuyerTotalAmountCheckOut'),
    path('StartBlockChainTransaction/', buyer.StartBlockChainTransaction, name='StartBlockChainTransaction'),
    path('BuyerViewPurchasedDetails/', buyer.BuyerViewPurchasedDetails, name='BuyerViewPurchasedDetails'),
    path('BuyerViewTransactinDetails/',buyer.BuyerViewTransactinDetails, name='BuyerViewTransactinDetails'),



    ### Admin Side Views
    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path("ViewSellersRegisteredUsers/", admins.ViewSellersRegisteredUsers, name="ViewSellersRegisteredUsers"),
    path("AdminActivaSellersUsers/", admins.AdminActivaSellersUsers, name="AdminActivaSellersUsers"),
    path("ViewBuyersRegisteredUsers/", admins.ViewBuyersRegisteredUsers, name="ViewBuyersRegisteredUsers"),
    path("AdminActivaBuyerssUsers/", admins.AdminActivaBuyerssUsers, name="AdminActivaBuyerssUsers"),
    path("AdminViewAllPurchased/", admins.AdminViewAllPurchased, name="AdminViewAllPurchased"),
    path('AdminViewAllBlockChainData', admins.AdminViewAllBlockChainData, name='AdminViewAllBlockChainData'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
