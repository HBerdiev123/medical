from django.shortcuts import render, get_object_or_404
from .models import Doctor

# Create your views here.
def list(request):
	docs = Doctor.objects.all()
	# docs = []
	return render(request, 'doctor-list.html', {'docs':docs})


def detail(request, slug):
	doc = get_object_or_404(Doctor, slug=slug)
	return render(request, 'doctor-detail.html', {'doc':doc})	