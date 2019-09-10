from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ['slug', 'author', 'timestamp']
	list_filter = ['author', 'timestamp']
	prepopulated_fields = {'slug':['title']}
	search_fields = ['title', 'slug', 'description']
	ordering		= ['author', 'timestamp']

admin.site.register(Post, PostAdmin)