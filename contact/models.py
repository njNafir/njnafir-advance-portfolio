from django.db import models
from njNafir.mixins import get_unique_path

PROJECT_COMPLETION = (
		('As soon as posible', 'As soon as posible'),
		('In 7 days', 'In 7 days'),
		('In 15 days', 'In 15 days'),
		('In 30 days', 'In 30 days'),
		('Not sure/To be determined/Talk you later', 'Not sure/To be determined/Talk you later')
	)

class HireContact(models.Model):
	name 				= models.CharField(max_length=32)
	email 				= models.EmailField()
	website 			= models.CharField(max_length=120, blank=True, null=True)
	project_budget 		= models.CharField(max_length=120)
	completion_date 	= models.CharField(max_length=32, choices=PROJECT_COMPLETION, default='Not sure/To be determined/Talk you later', blank=True, null=True)
	project_detail 		= models.TextField()
	timestamp 			= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email

class NormalContact(models.Model):
	name 		= models.CharField(max_length=32)
	email 		= models.EmailField()
	message 	= models.TextField(default='I want to work with you. Possible?')
	timestamp 	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

def social_contact_icon_path(instance, filename):
	up = get_unique_path()
	path = "social_icon/{u}/{f}".format(u=up, f=filename)
	return path

class SocialContactQuery(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

class SocialContactObjectManager(models.Manager):
	def get_queryset(self):
		return SocialContactQuery(self.model, using=self._db)

class SocialContact(models.Model):
	title 		= models.CharField(max_length=20)
	link 		= models.CharField(max_length=120)
	description = models.CharField(max_length=255)
	icon 		= models.FileField(upload_to=social_contact_icon_path)
	position 	= models.IntegerField(default='1')
	active 		= models.BooleanField(default=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)

	objects = SocialContactObjectManager()

	class Meta:
		ordering = [
			'position',
			'-timestamp'
		]

	def __str__(self):
		return self.title