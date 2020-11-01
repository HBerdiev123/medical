from django.shortcuts import render, get_object_or_404, redirect
from .models import Email
from .forms  import EmailForm
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.


# def index(request, flag="inbox"):
# 	emails = Email.objects.filter(status_choices=flag)
# 	return render(request, 'backoffice/pages/mailbox/mailbox.html', {'emails':emails})

def index(request, flag="inbox"):
	data = dict()
	print(request)
	emails = Email.objects.filter(status_choices=flag)
	if request.method =='GET':
		data['html_book_list'] = render_to_string('backoffice/pages/mailbox/partial_email_list.html', {
                'emails': emails
            })
		return JsonResponse(data)
	else:
		return render(request, 'backoffice/emails/list.html', {'emails':emails})
			
def list(request):
	emails = Email.objects.filter(status_choices='inbox')
	return render(request, 'backoffice/emails/list.html', {'emails':emails})

# def detail(request, pk):
# 	email  = Email.objects.get(id=pk)
# 	return render('backoffice/pages/mailbox/read_mail.html', {'email':email})


def compose(request):
	if request.method == "POST":
		form = EmailForm(request.POST)
		if form.is_valid():
			form.save()
		pass
	else:
		form = EmailForm()

	return render(request, 'backoffice/pages/mailbox/compose.html')


def read_mail(request, pk):
	email = Email.objects.get(id=pk)
	email.is_read = True
	email.save()
	return render(request, 'backoffice/emails/detail.html', {'email':email})


def delete_email(request, pk):
	result = {}

	if request.method == "POST":
		# pk = int(request.POST.get('id'))
		email  = get_object_or_404(Email, id=pk)
		status = email.delete()
		if status:
		# 	result = {'status':'ok'}
		# else:
		# 	result = {'status':'error'}
		# return JsonResponse(result)
			return list(request)
	else:
		pk = int(request.GET.get('id'))
		email  = get_object_or_404(Email, id=pk)
		print(email)
		result['html_form'] = render_to_string('backoffice/emails/partial_delete_confirm.html', 
			{'email':email})
		return JsonResponse(result)


def reply(request):
	data =  dict()
	if request.method=='POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			form.status_choices = 'sent'
			form.save()
	else:
		form = EmailForm()		
	data['html_form'] = render_to_string('backoffice/partial_email_form.html', {'form':form})	
	return JsonResponse(data)