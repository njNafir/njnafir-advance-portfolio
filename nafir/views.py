from django.shortcuts import render, Http404, redirect
from django.utils.http import is_safe_url
from .models import Info
from portfolio.models import Store, StoreProjectGalleryImage, StoreProjectFile
from blog.models import Post
from contact.forms import NormalContactForm
from contact.models import SocialContact

def home_page(request):
	info_ = Info.objects.first()
	stores_ = Store.objects.all()[:6]
	stores_gal_im_ = StoreProjectGalleryImage.objects.all()
	blog_post_ = Post.objects.all()[:8]
	form_ = NormalContactForm
	social_link = SocialContact.objects.all()
	home_page = True
	context = {
		'info':info_,
		'sts':stores_,
		'gal_im':stores_gal_im_,
		'bl_ps':blog_post_,
		'form':form_,
		'so_li': social_link,
		'home_page':home_page
	}
	ncf_post = NormalContactForm(request.POST or None)
	next_page = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_url = next_page or next_post or None
	if ncf_post.is_valid():
		instance = ncf_post.save(commit=False)
		instance.save()
		if is_safe_url(redirect_url, request.get_host()):
			return redirect(redirect_url)
	return render(request, 'pages/home.html', context)
