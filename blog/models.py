from django.db import models
from django.conf import settings
from django.urls import reverse
from njNafir.mixins import get_unique_path
from category.models import BlogCategory

User = settings.AUTH_USER_MODEL

def post_thumb_upload_path(instance, filename):
	unp = get_unique_path()
	path = "post_thum/{u}/{n}".format(u=unp, n=filename)
	return path

class Post(models.Model):
	title 			= models.CharField(max_length=255)
	slug 			= models.SlugField(max_length=120, unique=True)
	author 			= models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='md_nafir')
	thumbnail 		= models.ImageField(upload_to=post_thumb_upload_path)
	description 	= models.TextField()
	category		= models.ManyToManyField(BlogCategory)
	timestamp 		= models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('single_blog', args=[self.slug])
