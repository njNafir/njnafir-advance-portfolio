from django.contrib import admin
from django.urls import path, re_path, include
from .views import contact_page

urlpatterns = [
    re_path(r'^$', contact_page, name='contact_page'),
]
