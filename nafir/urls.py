from django.contrib import admin
from django.urls import re_path

from .views import home_page

urlpatterns = [
    re_path(r'^$', home_page, name='home_page'),
]