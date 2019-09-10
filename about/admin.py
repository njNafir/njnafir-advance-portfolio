from django.contrib import admin
from .models import ManOverview, Appointment, Qualification, Education, Interest, ResearchInterest, Award, Language, Membership

class TabAppointment(admin.TabularInline):
	model = Appointment
	extra = 0

class TabQualification(admin.TabularInline):
	model = Qualification
	extra = 0

class TabEducation(admin.TabularInline):
	model = Education
	extra = 0

class TabInterest(admin.TabularInline):
	model = Interest
	extra = 0

class TabResearchInterest(admin.TabularInline):
	model = ResearchInterest
	extra = 0

class TabAward(admin.TabularInline):
	model = Award
	extra = 0

class TabLanguage(admin.TabularInline):
	model = Language
	extra = 0

class TabMembership(admin.TabularInline):
	model = Membership
	extra = 0

class AdminManOverview(admin.ModelAdmin):
	list_display = ['name', 'website', 'email', 'address_line_1']
	search_fields = ['name', 'website', 'email', 'address_line_1']

	inlines = [TabAppointment, TabQualification, TabEducation, TabInterest, TabResearchInterest, TabAward, TabLanguage, TabMembership]

admin.site.register(ManOverview, AdminManOverview)
