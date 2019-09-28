from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update({'class':'form-control first_name', 'placeholder':'Ex: Bd'})
		self.fields['last_name'].widget.attrs.update({'class':'form-control last_name', 'placeholder':'Ex: Task'})
		self.fields['email'].widget.attrs.update({'class':'form-control email', 'placeholder':'Ex: bdtask@gmail.com'})
		self.fields['phone'].widget.attrs.update({'class':'form-control phone', 'placeholder':'Ex: 01*******36'})
		self.fields['address'].widget.attrs.update({'class':'form-control text-light text-capitalize address'})
		self.fields['message'].widget.attrs.update({'class':'form-control text-light text-capitalize message'})

	class Meta:
		model = Contact

		fields = [
			'first_name',
			'last_name',
			'email',
			'phone',
			'address',
			'message',
		]