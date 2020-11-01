from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User 
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')

# Create your models here.

class Category(models.Model):
	category_name = models.CharField(max_length=100)
	slug          = models.SlugField(max_length=120)
	category_description = models.TextField(blank=True)

	def __str__(self):
		return self.category_name

class Post(models.Model):
	STATUS_CHOICES = (
			('draft','Draft'),
			('published','Published'),

		)
	objects   = models.Manager()
	published = PublishedManager()

	title		  = models.CharField(max_length=250)
	post_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	post_image    = models.ImageField(upload_to='blog/%Y/%m/%d/')
	slug   		  = models.SlugField(max_length=250, unique_for_date='publish')
	tags   		  = TaggableManager()
	author	      = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
	body   		  = RichTextField()
	publish  	  = models.DateTimeField(default=timezone.now)
	created 	  = models.DateTimeField(auto_now_add=True)
	updated       = models.DateTimeField(auto_now=True)
	status        = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', args=[self.slug])


class Comment(models.Model):
	post   = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author = models.CharField(max_length=50)
	email  = models.EmailField()
	body   = models.TextField()
	created= models.DateTimeField(auto_now_add=True)
	updated= models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=False)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return f'Comment by {self.name} on {self.post}'		


class Contact(models.Model):
	name 	   = models.CharField(max_length=50)
	email      = models.EmailField()
	phone      = models.CharField(max_length=15)
	subject    = models.CharField(max_length=100)
	message    = models.TextField()
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)