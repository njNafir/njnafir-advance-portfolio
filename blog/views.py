from django.shortcuts import render
from nafir.models import Info
from .models import Post
from contact.models import SocialContact
from category.models import BlogCategory

def blog_page(request):
	info_ = Info.objects.first()
	blog_post_ = Post.objects.all()
	bolg_cat  = BlogCategory.objects.filter(active=True)
	social_link = SocialContact.objects.all()
	context = {
		'info':info_,
		'bl_ct':bolg_cat,
		'bl_ps':blog_post_,
		'so_li': social_link,
	}
	return render(request, 'pages/blog.html', context)

def single_blog(request, slug, *args, **kwargs):
	info_ = Info.objects.first()
	blog_post = Post.objects.get(slug=slug)
	social_link = SocialContact.objects.all()
	context = {
		'info':info_,
		'post':blog_post,
		'so_li': social_link,
	}
	return render(request, 'pages/single.html', context)

def blog_by_category(request, name, *args, **kwargs):
	info_ = Info.objects.first()
	blog_post_ = Post.objects.filter(category__name=name)
	bolg_cat  = BlogCategory.objects.filter(active=True)[:10]
	social_link = SocialContact.objects.all()
	context = {
		'info':info_,
		'bl_ct':bolg_cat,
		'bl_ps':blog_post_,
		'so_li': social_link,
	}
	return render(request, 'pages/blog.html', context)