from django.contrib import admin
from django.urls import path, re_path, include
from .views import contact_page

urlpatterns = [
    path('', contact_page, name='api_contact_page'),
]
