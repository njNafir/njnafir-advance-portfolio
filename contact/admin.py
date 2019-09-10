from django.contrib import admin

from .models import HireContact, NormalContact, SocialContact

class AdminHireContact(admin.ModelAdmin):
	list_display 	= ['name', 'email', 'website', 'project_budget', 'completion_date']
	list_filter 	= ['timestamp', 'completion_date']
	ordering 		= ['-timestamp', 'completion_date']
	search_fields	= ['name', 'email', 'project_detail']

admin.site.register(HireContact, AdminHireContact)

class AdminNormalContact(admin.ModelAdmin):
	list_display 	= ['name', 'email']
	list_filter 	= ['timestamp']
	ordering 		= ['-timestamp']
	search_fields	= ['name', 'email', 'description']

admin.site.register(NormalContact, AdminNormalContact)


class AdminSocialContact(admin.ModelAdmin):
	list_display 	= ['title', 'link', 'active']
	list_filter 	= ['active']
	ordering 		= ['-timestamp']
	search_fields	= ['title', 'link', 'description']

admin.site.register(SocialContact, AdminSocialContact)