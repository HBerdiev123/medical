from django import template 
from ..models import Email


register = template.Library()

@register.simple_tag
def unread_mails():
	return Email.objects.filter(is_read=False).count()

@register.simple_tag
def drafts():
	return Email.objects.filter(status_choices='draft').count()	

@register.simple_tag
def starred():
	return Email.objects.filter(status_choices='starred').count()		