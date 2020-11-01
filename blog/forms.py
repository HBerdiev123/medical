from django.forms import ModelForm 
from .models import Comment
from .models import Contact
from django import forms


class CommentForm(ModelForm):
	class Meta:
		model  = Comment
		fields = ['author', 'email', 'body',]



class ContactForm(ModelForm):
	class Meta:
		model  = Contact
		fields = ['name', 'email', 'subject', 'phone', 'message']


class SearchForm(forms.Form):
	query = forms.CharField() 	