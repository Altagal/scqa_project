from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('gestao.urls')),
    path('', include('home.urls')),

]
