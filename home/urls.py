
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.displayPrivacyPolicy, name='privacy-policy'),
    path('terms-conditions/', views.displayTermsConditions, name='t&c'),
    path('newsletter/', views.subscribe, name='subscribe'),
]
