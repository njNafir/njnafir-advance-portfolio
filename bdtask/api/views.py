from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from bdtask.models import Contact
from .serializers import ContactCreateSerializer, ContactUpdateSerializer, ContactDetailSerializer, ContactListSerializer
from .pagination import ContactLimitOffsetPagination, ContactPageNumberPagination

class ContactCreateAPIView(CreateAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactCreateSerializer

class ContactDeleteAPIView(DestroyAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactDetailSerializer

class ContactDetailAPIView(RetrieveUpdateAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactDetailSerializer

class ContactListAPIView(ListAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactListSerializer
	pagination_class = ContactPageNumberPagination #ContactLimitOffsetPagination
	# print("Start")
	# for q in queryset:
	# 	print(q.get_email)
	# print("End")

class ContactUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactUpdateSerializer