from django.contrib import admin
from .models import BlogCategory

class AdminBlogCategory(admin.ModelAdmin):
	list_display 	= ['name', 'active', 'position', 'updated', 'timestamp']
	list_filter 	= ['active', 'updated', 'timestamp']
	search_fields 	= ['name', 'blog']
	ordering 		= ['active', 'position', 'updated', 'timestamp']

admin.site.register(BlogCategory, AdminBlogCategory)