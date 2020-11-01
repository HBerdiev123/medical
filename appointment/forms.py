from django.forms import ModelForm
from .models import Appointment, Schedule

class AppointmentForm(ModelForm):
	class Meta:
		model  = Appointment
		fields = ('name', 'email', 'phone', 'service', 'doctor', 'age')



class ScheduleForm(ModelForm):
	class Meta:
		model  = Schedule
		fields = ('appointment', 'date_of_appointment')
