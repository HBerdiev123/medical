from django.conf.urls import url
from django.urls import path
from . import views
app_name ='blog'

urlpatterns = [
	path('', views.list, name='list'),
	path('<slug:slug>', views.detail, name='detail'),
	path('tag/<slug:tag_slug>/', views.list, name='post_list_by_tag'), 
	path('cat/<slug:cat_slug>/', views.list, name='list_post_by_category'), 
]