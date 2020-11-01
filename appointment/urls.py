from django.conf.urls import url
from django.urls import path
from . import views

app_name ='appointment'
urlpatterns = [
	path('', views.appointment, name='appointment'),
	path('create/', views.create, name='app-create'), 
	url(r'(?P<pk>\d+)/delete/$', views.appointment_delete, name="delete"),
	path('create_schedule/<int:pk>', views.create_schedule, name='sche-create'), 
	path('update_schedule/<int:pk>', views.update_schedule, name='sche-update'), 
	path('schedule/<int:pk>/delete', views.schedule_delete, name="sche-delete"),
	url(r'(?P<pk>\d+)/update/$', views.appointment_update, name="app-update"),
	path('test/', views.test, name='test'),
	path('step/', views.step1, name='step'),
	path('forma/', views.forma, name='forma'),
	path('<int:id>', views.detail, name='appointment_detail'),
]

