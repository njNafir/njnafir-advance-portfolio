from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class ContactLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 1
	max_limit = 10

class ContactPageNumberPagination(PageNumberPagination):
	page_size = 10