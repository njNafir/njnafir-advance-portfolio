from django.contrib import admin
from django.urls import re_path

from .views import about_page

urlpatterns = [
    re_path(r'^about/$', about_page, name='about_page'),
]