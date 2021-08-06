"""diginotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path , include
from .views.home import HomeView, about, contactus, enquiry, search
from .views.auth import  SignupView, LoginView, logout_view
from .views.details import ProductDetailView
from .views.checkout import checkout
from .views.payment import create_payment, payment_verify
from .views.order import OrderListView

urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),
    path('about', about),
    path('contactus', contactus),
    path('enquiry', enquiry),
    path('search', search, name='search'),
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('product/<str:slug>', ProductDetailView.as_view()),
    path('checkout/<str:slug>', checkout, name='checkout'),
    path('payment/verify', payment_verify, name='verify_payment'),
    path('payment/<str:slug>', create_payment, name='create_payment'),
    path('orders', OrderListView.as_view(), name='orders'),
    
    
]
