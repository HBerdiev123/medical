from django.urls import path, include, re_path
from . import views
from appointment import views as ap_views

app_name ='backoffice'

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('new_appointment/', ap_views.new_appointment, name='new'),
	path('all_appointments/', ap_views.all_appointments, name='all'),
	path('pending_appointments/', ap_views.pending_appointments, name='pending'),
	path('email/', views.emailto, name='email'),
	
]