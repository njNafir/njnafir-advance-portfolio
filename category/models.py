from django.db import models
from django.urls import reverse

class BlogCategory(models.Model):
	name 		= models.CharField(max_length=20)
	position 	= models.IntegerField()
	active 		= models.BooleanField()
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = [
			'position', 
			'-timestamp', 
			'-updated'
		]

	def __str__(self):
		return self.name

	def get_cat_url(self):
		return reverse('blog_by_category', args=[self.name])