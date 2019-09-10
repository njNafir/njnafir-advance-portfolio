from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.core.files.storage import FileSystemStorage

LAVEL_SCALE = (
		('Beginner', 'beginner'),
		('Elementary', 'elementary'),
		('Intermediate', 'intermediate'),
		('Advanced', 'advanced')
	)

class Skill(models.Model):
	position			= models.IntegerField(blank=True, null=True)
	prog_class 			= models.CharField(max_length=120, blank=True, null=True)
	prog_bar_class 		= models.CharField(max_length=120, blank=True, null=True)
	prog_info 			= models.CharField(max_length=120)
	area_valuemin 		= models.IntegerField(default='0')
	area_valuemax 		= models.IntegerField(default='100')
	prog_info_perc 		= models.IntegerField(default='15')
	prog_skill_perc 	= models.IntegerField()
	show_prog_skill 	= models.IntegerField(blank=True, null=True)
	prog_skill_lavel	= models.CharField(max_length=120, choices=LAVEL_SCALE, default='Intermediate')
	timestamp 			= models.DateTimeField(auto_now_add=True)
	updated 			= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['position', '-prog_skill_perc', '-timestamp']

	def __str__(self):
		return self.prog_info

def skill_pre_save_connector(sender, instance, *args, **kwargs):
	if not instance.position:
		klass_ = instance.__class__
		max_ = klass_.objects.all().count()
		instance.position = max_ + 1

	if instance.prog_info_perc and instance.prog_skill_perc:
		inf_per = instance.prog_info_perc
		sk_per = instance.prog_skill_perc
		show_per = inf_per + sk_per
		instance.show_prog_skill = show_per

pre_save.connect(skill_pre_save_connector, sender=Skill)

def favicon_upload_path(instance, filename):
	path = "img/favicon.ico"
	return path

def profile_picture_upload_path(instance, filename):
	path = "img/{fn}".format(fn=filename)
	return path

class Info(models.Model):
	title 				= models.CharField(max_length=255, default='Nj Nafir')
	favicon 			= models.ImageField(upload_to=favicon_upload_path, storage=FileSystemStorage(location=settings.MAIN_ROOT))
	name 				= models.CharField(max_length=120, default='Nj Nafir')
	picture 			= models.ImageField(upload_to=profile_picture_upload_path, storage=FileSystemStorage(location=settings.MAIN_ROOT))
	description 		= models.CharField(max_length=120, default='Full Stack Web Developer')
	view_portfolio_text = models.CharField(max_length=120, default='View Portfolio')
	hire_me_text 		= models.CharField(max_length=120, default='Hire Me')
	about_intro_text 	= models.CharField(max_length=255, default="I'm Nattachiuj Jaman Nafir")
	exper_sec_title 	= models.CharField(max_length=120, default="Working with:")
	exper_skill 		= models.ManyToManyField(Skill, blank=True)
	exper_comment 		= models.TextField(default="I'm expert for this Full Stack Web Development career")
	about_more_text 	= models.CharField(max_length=120, default='About More')
	store_more_text 	= models.CharField(max_length=120, default='Portfolio More')
	store_d_more_text	= models.CharField(max_length=120, default='Show More')
	post_more_text		= models.CharField(max_length=120, default='Blog More')
	timestamp 			= models.DateTimeField(auto_now_add=True)
	updated 			= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

