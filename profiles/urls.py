from django.conf.urls import url
from django.urls 	  import path, include, re_path
from . import views 

app_name = 'profile'
urlpatterns = [
	path('', views.index, name="profile"),
]