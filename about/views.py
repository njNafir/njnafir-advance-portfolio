from django.shortcuts import render
from nafir.models import Info
from contact.models import SocialContact
from .models import ManOverview, Appointment, Qualification, Education, Interest, ResearchInterest, Award, Language, Membership

def about_page(request):
	info_ = Info.objects.first()
	social_link = SocialContact.objects.all()
	man_overview = ManOverview.objects.first()
	appointment = Appointment.objects.filter(man_overview_id=man_overview.id)
	qualification = Qualification.objects.filter(man_overview_id=man_overview.id)
	education = Education.objects.filter(man_overview_id=man_overview.id)
	interest = Interest.objects.filter(man_overview_id=man_overview.id)
	research_interest = ResearchInterest.objects.filter(man_overview_id=man_overview.id)
	award = Award.objects.filter(man_overview_id=man_overview.id)
	language = Language.objects.filter(man_overview_id=man_overview.id)
	membership = Membership.objects.filter(man_overview_id=man_overview.id)
	context = {
		'info': info_,
		'so_li': social_link,
		'man_overview': man_overview,
		'appointment': appointment,
		'qualification': qualification,
		'education': education,
		'interest': interest,
		'research_interest': research_interest,
		'award': award,
		'language': language,
		'membership': membership
	}
	return render(request, 'pages/about.html', context)