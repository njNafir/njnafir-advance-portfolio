from django.contrib import admin

from .models import Skill, Info

class AdminSkill(admin.ModelAdmin):
	list_display = ['prog_info', 'position', 'area_valuemin', 'area_valuemax', 'prog_info_perc', 'prog_skill_perc']
	list_filter = ['prog_info_perc', 'prog_skill_perc']
	ordering = ['position', '-prog_skill_perc', '-timestamp']
	search_fields = ['prog_info']

admin.site.register(Skill, AdminSkill)

class AdminInfo(admin.ModelAdmin):
	list_display = ['timestamp', 'updated']
	list_filter = ['timestamp', 'updated']
	ordering = ['-timestamp']
	search_fields = ['title', 'name', 'description']

admin.site.register(Info, AdminInfo)
