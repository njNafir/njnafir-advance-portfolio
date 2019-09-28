from django.contrib import admin
from .models import Contact

class AdminContact(admin.ModelAdmin):
	list_display 	= ['email', 'phone', 'isActive']
	list_filter 	= ['isActive']
	ordering 		= ['-createdAt', 'isActive']
	search_fields	= ['first_name', 'last_name', 'email', 'phone', 'address', 'description']

admin.site.register(Contact, AdminContact)
