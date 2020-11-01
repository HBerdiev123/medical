from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

app_name ="emails"
urlpatterns = (
	path('', views.list, name='list'),
	path('flag/<str:flag>', views.index, name='list-flag'),
	path('create/', views.compose, name="compose"),
	path('read/<int:pk>/', views.read_mail, name="read"),
	path('delete/', views.delete_email, name="delete"),
	path('delete/<int:pk>', views.delete_email, name="delete"),
	path('detail/<int:pk>/', views.read_mail, name="detail"),

)