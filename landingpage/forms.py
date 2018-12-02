from django import forms
from django.forms import Textarea
from django.core import validators
from .models import Contact 

class ContactForm(forms.ModelForm):
	

	class Meta():
		model = Contact 
		exclude = ['created_date']
		
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['email'].widget.attrs.update({'placeholder': 'Email address',
												   'class': 'form-control',
												   'name':'email',
												   'required':''})
		self.fields['name'].widget.attrs.update({'placeholder': "Full Name",
												 'class': 'form-control',
												 'name':'name',
												 'required':""})
		self.fields['message'].widget.attrs.update({'class':'form-control',
													'rows':8,
													'placeholder': "Your message",
													'name': 'message',
													'require':''})






		 
		
		

