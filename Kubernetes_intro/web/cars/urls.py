from django.contrib import admin
from django.urls import path, include
from cars.views import *

app_name = 'Car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view())
]