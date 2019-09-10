from django import forms
from .models import NormalContact, HireContact

class HireContactForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class':'form-control name', 'placeholder':'Ex: Nj Nafir'})
		self.fields['email'].widget.attrs.update({'class':'form-control email', 'placeholder':'Ex: mdanjenafir24434@gmail.com'})
		self.fields['website'].widget.attrs.update({'class':'form-control website', 'placeholder':'Ex: njnafir.com'})
		self.fields['project_budget'].widget.attrs.update({'class':'form-control budget', 'placeholder':'Ex: $500 (Five hundred dollar)'})
		self.fields['completion_date'].widget.attrs.update({'class':'form-control date', 'placeholder':'Ex: Select one of theme'})
		self.fields['project_detail'].widget.attrs.update({'class':'form-control detail'})

	class Meta:
		model = HireContact

		fields = [
			'name',
			'email',
			'website',
			'project_budget',
			'completion_date',
			'project_detail'
		]

class NormalContactForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class':'form-control name', 'placeholder':'Ex: Nj Nafir'})
		self.fields['email'].widget.attrs.update({'class':'form-control email', 'placeholder':'Ex: mdanjenafir24434@gmail.com'})
		self.fields['message'].widget.attrs.update({'class':'form-control text-light text-capitalize message'})

	class Meta:
		model = NormalContact

		fields = [
			'name',
			'email',
			'message'
		]