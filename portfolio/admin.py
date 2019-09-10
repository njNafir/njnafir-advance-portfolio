from django.contrib import admin
from .models import Store, StoreProjectGalleryImage, StoreProjectFile

class StorePGImageTabularAdmin(admin.TabularInline):
	model = StoreProjectGalleryImage
	extra = 1

class StorePFileTabularAdmin(admin.TabularInline):
	model = StoreProjectFile
	extra = 1


class StoreAdmin(admin.ModelAdmin):
	list_display = ['title', 'project_type', 'web_link', 'timestamp']
	list_filter = ['project_type', 'used_skill', 'updated', 'timestamp']
	prepopulated_fields = {'slug':['title']}
	search_fields = ['title', 'subtitle', 'description', 'web_link']
	ordering = ['-updated', '-timestamp']

	inlines = [StorePGImageTabularAdmin, StorePFileTabularAdmin]

admin.site.register(Store, StoreAdmin)
