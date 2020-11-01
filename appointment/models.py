from django.db import models
from doctors.models import Doctor
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Appointment(models.Model):
	services = (
			('dental',"Dentail Care"),
			('neurology','Neurology'),
			('cardiology','Cardiology'),
			('pathalogy','Pathology'),
		)

	statuses = (('pending', 'Pending'),('processed', 'Processed'),)

	name 	   = models.CharField(max_length=50)
	email      = models.EmailField()
	phone 	   = models.CharField(max_length=20)
	service    = models.CharField(max_length=15, choices=services, default='dental')
	doctor     = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	age   	   = models.IntegerField()
	comments   = models.TextField(blank=True)
	status 	   = models.CharField(max_length=10, choices=statuses, default='pending')
	created_at = models.DateTimeField(auto_now_add=True)
	update_at  = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ('-created_at', 'status')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('appointment:appointment_detail', args=[self.id])		



class Schedule(models.Model):
	appointment = models.OneToOneField(Appointment, on_delete=models.SET_NULL, blank=True, null=True, related_name='schedule')
	date_of_appointment = models.DateTimeField(default=timezone.now)
	created= models.DateTimeField(auto_now_add=True)
	updated= models.DateTimeField(auto_now=True)