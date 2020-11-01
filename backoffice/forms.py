from django.forms import ModelForm
from emails.models import Email
# from urllib import request

# class EmailForm(ModelForm):
# 	class Meta:
# 		model  = Email
# 		fields = ('sender', 'email_to', 'subject', 'body')

		# def save(self, force_insert=False, force_update=False, commit=True):
		# 	Email = super().save(commit=False)
		# 	Email.user = request.user

		# 	if commit:
		# 		Email.save()
		# 	return Email		

		