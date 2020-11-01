from django.db   import models
from django.conf import settings
from urllib      import request

# Create your models here.


# class Email(models.Model):
# 	user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='email_author')
# 	email_to   = models.EmailField()
# 	subject    = models.CharField(max_length=150)
# 	body       = models.TextField()
# 	created_at = models.DateTimeField(auto_now_add=True)


# 	class Meta:
# 		ordering = ('-created_at',)

# 	def __str__(self):
# 		return f'Email to {self.email_to} on {self.created_at} by {self.user}' 		

	# def save(self, *args, **kwargs):
	# 	self.user = request.user
	# 	super(Email, self).save(*args, **kwargs)
