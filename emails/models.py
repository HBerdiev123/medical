from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
class Email(models.Model):

	STATUS_CHOICES = (
			('draft','Draft'),
			('inbox','Inbox'),
			('sent', 'Sent'),
			('starred', 'Starred'),
			('trash','Trash')
		)

	sender         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='email_author')
	email_to   	   = models.EmailField()
	subject    	   = models.CharField(max_length=150)
	body       	   = RichTextField()
	created_at 	   = models.DateTimeField(auto_now_add=True)
	status_choices = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	is_read        = models.BooleanField(default=False)


	class Meta:
		ordering   = ('-created_at',)

	def __str__(self):
		return f'Email to {self.email_to} on {self.created_at} by {self.sender}' 	