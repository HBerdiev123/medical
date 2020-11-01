from django.contrib import admin
from .models import Doctor
from parler.admin import TranslatableAdmin

# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(TranslatableAdmin):
	list_display = ('name', 'degree', 'specialization')
	prepopulated_fields = {'slug':('name',)}