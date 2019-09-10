from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class ManOverview(models.Model):
	name 				= models.CharField(max_length=30)
	website 			= models.CharField(max_length=30, blank=True, null=True)
	address_line_1 		= models.CharField(max_length=120)
	address_line_2 		= models.CharField(max_length=120, blank=True, null=True)
	email 				= models.EmailField()
	phone 				= models.DecimalField(decimal_places=0, max_digits=13)
	objective			= models.TextField(blank=True, null=True)

class Appointment(models.Model):
	man_overview 		= models.ForeignKey(ManOverview, on_delete=models.CASCADE)
	position 			= models.CharField(max_length=120)
	institute 			= models.CharField(max_length=120)
	department 			= models.CharField(max_length=120, blank=True, null=True)
	start_date 			= models.CharField(max_length=12, blank=True, null=True)
	end_date 			= models.CharField(max_length=12, blank=True, null=True)

def qualification_certificate_upload_path(instance, filename):
	path = "secr_top/about_f/quali/{filename}".format(filename=filename)
	return path

class Qualification(models.Model):
	man_overview 		= models.ForeignKey(ManOverview, on_delete=models.CASCADE)
	course_name 		= models.CharField(max_length=120)
	certificate 		= models.FileField(upload_to=qualification_certificate_upload_path, storage=FileSystemStorage(location=settings.PROT_ROOT), blank=True, null=True)


def education_certificate_upload_path(instance, filename):
	path = "secr_top/about_f/edu/{filename}".format(filename=filename)
	return path

class Education(models.Model):
	man_overview 		= models.ForeignKey(ManOverview, on_delete=models.CASCADE)
	degree 				= models.CharField(max_length=40)
	subject 			= models.CharField(max_length=120)
	year 				= models.DecimalField(decimal_places=0, max_digits=4, blank=True, null=True)
	institute 			= models.CharField(max_length=120, blank=True, null=True)
	result 				= models.DecimalField(decimal_places=2, max_digits=3, blank=True, null=True)
	certificate 		= models.FileField(upload_to=education_certificate_upload_path, storage=FileSystemStorage(location=settings.PROT_ROOT), blank=True, null=True)

class Interest(models.Model):
	man_overview 		= models.ForeignKey(ManOverview, on_delete=models.CASCADE)
	interest_name 		= models.CharField(max_length=32)
	interest_type 		= models.CharField(max_length=20, blank=True, null=True)

class ResearchInterest(models.Model):
	man_overview 		= models.ForeignKey(ManOverview, on_delete=models.CASCADE)
	name 				= models.CharField(max_length=120)
	description 		= models.TextField(blank=True, null=True)

def award_certificate_upload_path(instance, filename):
	path = "secr_top/about_f/award/{filename}".format(filename=filename)
	return path

class Award(models.Model):
	man_overview 		= models.ForeignKey(ManOverview, on_delete=models.CASCADE)
	award_detail 		= models.CharField(max_length=255)
	prove_file			= models.FileField(upload_to=award_certificate_upload_path, storage=FileSystemStorage(location=settings.PROT_ROOT), blank=True, null=True)

class Language(models.Model):
	man_overview 		= models.ForeignKey(ManOverview, on_delete=models.CASCADE)
	language	 		= models.CharField(max_length=20)

class Membership(models.Model):
	man_overview 		= models.ForeignKey(ManOverview, on_delete=models.CASCADE)
	in_detail 			= models.CharField(max_length=255)