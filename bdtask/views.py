from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from bdtask.models import Contact
from .forms import ContactForm

def contact_page(request):
	form_ = ContactForm
	context = {
		'form':form_,
	}
	ncf_post = ContactForm(request.POST or None)
	next_page = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_url = next_page or next_post or None
	if ncf_post.is_valid():
		instance = ncf_post.save(commit=False)
		instance.save()
		if is_safe_url(redirect_url, request.get_host()):
			return redirect(redirect_url)

	return render(request, 'contact.html', context)