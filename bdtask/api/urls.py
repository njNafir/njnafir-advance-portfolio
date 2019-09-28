from django.contrib import admin
from django.urls import path, re_path
from bdtask.api.views import ContactListAPIView, ContactCreateAPIView, ContactDeleteAPIView, ContactDetailAPIView, ContactUpdateAPIView

urlpatterns = [
	re_path(r'^$', ContactListAPIView.as_view(), name='list_api'),
    re_path(r'^create/$', ContactCreateAPIView.as_view(), name='create_api'),
    re_path(r'^(?P<pk>\d+)/$', ContactDetailAPIView.as_view(), name='detail_api'),
    re_path(r'^(?P<pk>\d+)/edit/$', ContactUpdateAPIView.as_view(), name='update_api'),
    re_path(r'^(?P<pk>\d+)/delete/$', ContactDeleteAPIView.as_view(), name='delete_api'),
]