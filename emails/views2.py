from django.shortcuts import render, get_object_or_404
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
		return render(request, 'backoffice/pages/mailbox/mailbox.html', {'emails':emails})
			
def list(request):
	emails = Email.objects.filter(status_choices='inbox')
	return render(request, 'backoffice/pages/mailbox/mailbox.html', {'emails':emails})

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
	# email.is_read = True
	# email.save()
	return render(request, 'backoffice/pages/mailbox/read-mail.html', {'email':email})


def delete_email(request):
	print(request.GET)
	# email = get_object_or_404(Email, id=pk)
	# email.delete()

	return JsonResponse({'ok':'ok'})