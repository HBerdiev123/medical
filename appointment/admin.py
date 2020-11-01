from django.contrib import admin
from .models import Appointment, Schedule
# Register your models here.


admin.site.register(Appointment)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
	list_display = ['appointment', 'date_of_appointment']