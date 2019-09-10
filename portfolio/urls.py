from django.contrib import admin
from django.urls import path, re_path
from .views import portfolio_all, portfolio_full_stack, portfolio_developed, portfolio_designed, portfolio_single

urlpatterns = [
	re_path(r'^portfolio/$', portfolio_all, name='portfolio_all'),
	re_path(r'^portfolio/dev-des/$', portfolio_full_stack, name='portfolio_full_stack'),
	re_path(r'^portfolio/dev/$', portfolio_developed, name='portfolio_developed'),
	re_path(r'^portfolio/des/$', portfolio_designed, name='portfolio_designed'),
	re_path(r'^portfolio/(?P<slug>[-\w]+)$', portfolio_single, name='portfolio_single')
]