from django.shortcuts import render, redirect, get_object_or_404
from nafir.models import Info
from portfolio.models import Store, StoreProjectGalleryImage, StoreProjectFile
from contact.models import SocialContact

def get_others():
	info_ = Info.objects.first()
	stores_ = Store.objects.all()
	stores_gal_im_ = StoreProjectGalleryImage.objects.all()
	social_link = SocialContact.objects.all()
	return info_, stores_, stores_gal_im_, social_link

def portfolio_all(request):
	info_, stores_, stores_gal_im_, social_link = get_others()
	context = {
		'portfolio_all': portfolio_all,
		'info':info_,
		'sts':stores_,
		'gal_im':stores_gal_im_,
		'so_li': social_link,
	}
	return render(request, 'pages/portfolio.html', context)

def portfolio_full_stack(request):
	info_, stores_, stores_gal_im_, social_link = get_others()
	stores_ = stores_.filter(project_type='Full Stack')
	context = {
		'info':info_,
		'sts':stores_,
		'gal_im':stores_gal_im_,
		'so_li': social_link,
	}
	return render(request, 'pages/portfolio.html', context)

def portfolio_developed(request):
	info_, stores_, stores_gal_im_, social_link = get_others()
	stores_ = stores_.filter(project_type='Web Development')
	context = {
		'info':info_,
		'sts':stores_,
		'gal_im':stores_gal_im_,
		'so_li': social_link,
	}
	return render(request, 'pages/portfolio.html', context)

def portfolio_designed(request):
	info_, stores_, stores_gal_im_, social_link = get_others()
	stores_ = stores_.filter(project_type='Web Design')
	context = {
		'info':info_,
		'sts':stores_,
		'gal_im':stores_gal_im_,
		'so_li': social_link,
	}
	return render(request, 'pages/portfolio.html', context)

def portfolio_single(request, slug, *args, **kwargs):
	info_, stores_, stores_gal_im_, social_link = get_others()
	store = Store.objects.get(slug=slug)
	single = True
	context = {
		'portfolio_all': portfolio_all,
		'info':info_,
		'st':store,
		'gal_im':stores_gal_im_,
		'so_li': social_link,
		'single': single
	}
	return render(request, 'pages/portfolio.html', context)