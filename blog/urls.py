from django.contrib import admin
from django.urls import re_path
from .views import blog_page, single_blog, blog_by_category

urlpatterns = [
	re_path(r'^blog/$', blog_page, name='blog_page'),
	re_path(r'^blog/cat-(?P<name>[-\w]+)$', blog_by_category, name='blog_by_category'),
	re_path(r'^blog/(?P<slug>[-\w]+)$', single_blog, name='single_blog'),
]

