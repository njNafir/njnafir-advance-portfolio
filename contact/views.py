from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from nafir.models import Info
from .forms import NormalContactForm, HireContactForm
from contact.models import SocialContact

def contact_page(request):
	info_ = Info.objects.first()
	form_ = NormalContactForm
	hire_form_ = HireContactForm
	social_link = SocialContact.objects.all()
	context = {
		'info':info_,
		'form':form_,
		'hire_form':hire_form_,
		'so_li': social_link,
	}
	ncf_post = NormalContactForm(request.POST or None)
	hcf_post = HireContactForm(request.POST or None)
	next_page = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_url = next_page or next_post or None
	if ncf_post.is_valid():
		instance = ncf_post.save(commit=False)
		instance.save()
		if is_safe_url(redirect_url, request.get_host()):
			return redirect(redirect_url)

	if hcf_post.is_valid():
		instance = hcf_post.save(commit=False)
		instance.save()
		if is_safe_url(redirect_url, request.get_host()):
			return redirect(redirect_url)
	return render(request, 'pages/contact.html', context)