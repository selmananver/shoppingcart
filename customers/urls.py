from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('account', views.showaccount,name='account'),
     path('signout', views.signout,name='signout'),
]