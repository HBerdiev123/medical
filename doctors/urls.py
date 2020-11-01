from django.urls import path
from . import views

app_name ='doctors'
urlpatterns = [
	path('', views.list, name = 'list'),
	path('<slug:slug>', views.detail, name='detail'),
]