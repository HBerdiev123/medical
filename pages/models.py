from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User 
from django.utils.safestring import mark_safe
import markdown

# Create your models here.
class PageCategory(models.Model):
	category_name        = models.CharField(max_length=30, unique=True)
	category_description = models.TextField(blank=True)

	def __str__(self):
		return self.category_name


class Page(models.Model):
	
	def save(self, *args, **kargs):
		self.body = mark_safe(markdown.markdown(self.body))
		# print(self.body)
		super(Page, self).save(*args, **kargs)
		


	STATUS_CHOICES = (
		('draft','Draft'),
		('published','Published'),

	)

	title	      = models.CharField(max_length=70)
	page_category = models.ForeignKey(PageCategory, on_delete=models.SET_NULL, blank=True, null=True, related_name='pages')
	slug  	   	  = models.SlugField()
	priority   	  = models.IntegerField()
	body 	      = RichTextUploadingField()
	author	      = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at    = models.DateTimeField(auto_now_add=True)
	updated_at    = models.DateTimeField(auto_now=True)
	status        = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')



	class Meta:
		ordering = ('-updated_at',)
	
	def __str__(self):
		return self.title