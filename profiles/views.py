from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
	user = get_user_model()
	return render(request, 'backoffice/profile/profile.html',{'user':user})