from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
	path('<slug:slug>', views.page, name='page'),
]