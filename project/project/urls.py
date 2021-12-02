"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api.views import CustomerView, RestaurantListView, RestaurantDetailView, MenuItemView
from api.views import OrderView, GetOtpView, VerifyOtpView
from rest_framework.routers import SimpleRouter
from django.urls.conf import include

router = SimpleRouter()
router.register('items', MenuItemView)
router.register('customer', CustomerView)
router.register('restdetail', RestaurantDetailView)
router.register('order', OrderView)

urlpatterns = [
    path('',include(router.urls)),
    path('restlist/', RestaurantListView.as_view()),
    path('getotp/', GetOtpView.as_view()),
    path('verifyotp/', VerifyOtpView.as_view()),
]
