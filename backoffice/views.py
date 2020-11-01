from django.shortcuts    import render
from django.http 	     import JsonResponse
from appointment.models  import Appointment
from emails.forms    import EmailForm 
from django.contrib.auth import get_user_model
from blog.models 		 import Post


# Create your views here.

def dashboard(request):
	appointments = Appointment.objects.all().order_by('-update_at')
	posts        = Post.objects.all()[:4]
	if request.method=='POST':
		email = EmailForm(request.POST)
	
		if email.is_valid():
			email.cleaned_data
			email.save()
		# return JsonResponse({'status':'success'})
		return render(request, 'backoffice/index.html')
	else:
		email = EmailForm(initial={'user':request.user.id})	
	return render(request, 'backoffice/index.html', {'appointments':appointments, 'form':email, 'posts':posts})


def emailto(request):
	if request.method=='POST':
		print(request.user.id)
		email = EmailForm(request.POST)
		if email.is_valid():
			email.cleaned_data
			email.save(commit=False)
			email.sender = request.user
			email.save()
		# return JsonResponse({'status':'success'})
		return render(request, 'backoffice/index.html')
	else:
		email = EmailForm()
	return render(request, 'backoffice/index.html', {'form':email})	


def inbox(request):
	return render(request, 'backoffice/inbox.html')


def sent(request):
	return render(request, 'backoffice/sent.html')

def drafts(request):
	return render(request, 'backoffice/drafts.html')

def trash(request):
	return render(request, 'backoffice/trash.html')				

	
