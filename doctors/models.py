from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.


class Doctor(TranslatableModel):
	
	translations = TranslatedFields(
			specialization = models.CharField(max_length=50),
			degree 		   = models.CharField(max_length=70, null=True),
			biography 	   = RichTextUploadingField(),
			contact_info   = RichTextField() 
		)

	name   		   = models.CharField(max_length=100)
	slug  		   = models.SlugField()
	doc_image      = models.ImageField(upload_to='doctors/')
	# specialization = models.CharField(max_length=50)
	# degree 		   = models.CharField(max_length=70, null=True)
	# biography 	   = RichTextUploadingField()
	# eduction  	   = RichTextField()
	# contact_info   = RichTextField() 
	created_at     = models.DateTimeField(auto_now_add=True)
	updated_at     = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name 

	
	def get_absolute_url(self):
		return reverse('doctor:detail', args=[self.slug])
