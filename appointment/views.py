from django.shortcuts       import render, get_object_or_404
from .forms 	            import AppointmentForm, ScheduleForm
from .models                import Appointment, Schedule
from django.core.paginator  import Paginator, EmptyPage, PageNotAnInteger
from django.http 		    import JsonResponse
from django.template.loader import render_to_string

# Create your views here.

def appointment(request):
	# new_appointment = None 
	# print(request.POST)
	if request.method =="POST":
		form  = AppointmentForm(data = request.POST)

		if form.is_valid():
			form.cleaned_data
			form.save()
	else:
		form = AppointmentForm()

	return render(request, 'index-2.html', {'form':form}) 	 

def save_appointment_form(request, form, template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			appointments = Appointment.objects.all()
			data['html_book_list'] = render_to_string('backoffice/partial_appointment_list.html', {
                'appointments': appointments
            })
		else:
			data['form_is_valid'] = False
	context = {'form': form}
	data['html_form'] = render_to_string(template_name, context, request=request)
	return JsonResponse(data)



def create(request):
	if request.method == "POST":
		form = AppointmentForm(request.POST)
	else:
		form = AppointmentForm()
	return save_appointment_form(request, form, 'backoffice/partial_appointment_create.html')		

def appointment_update(request, pk):
	appointment = get_object_or_404(Appointment, pk=pk)

	if request.method =='POST':
		form    = AppointmentForm(request.POST, instance=appointment)
	else:
		form    = AppointmentForm(instance=appointment)
	return save_appointment_form(request, form, 'backoffice/partial_appointment_update.html')	


def appointment_delete(request, pk):
	appointment = get_object_or_404(Appointment, pk=pk)
	data        = dict()

	if request.method =='POST':
		appointment.delete()
		data['form_is_valid']  = True
		appointments   = Appointment.objects.all()
		data['html_book_list'] = render_to_string('backoffice/partial_appointment_list.html', {
			'appointments':appointments
			})
	else:
		context = {'appointment':appointment}
		data['html_form']      = render_to_string('backoffice/partial_appointment_delete.html', 
			context, request=request,
			)
	return JsonResponse(data)


# To store Shedule Update and create modal 
def save_schedule_form(request, update, pk, form, template_name):
	data = dict()
	if not update:
		appointment = get_object_or_404(Appointment, id=pk)

	if request.method == 'POST':
		if form.is_valid():
			print(form.is_valid())
			form.save(commit=False)
			if not update:
				appointment.status = 'processed'
				appointment.save()
			form.save()
			data['form_is_valid'] = True
			appointments = Appointment.objects.all()
			data['html_book_list'] = render_to_string('backoffice/partial_appointment_list.html', {
                'appointments': appointments
            })
		else:
			data['form_is_valid'] = False
	context = {'form': form, 'app_id':pk}
	data['html_form'] = render_to_string(template_name, context, request=request)
	return JsonResponse(data)


def create_schedule(request, pk):
	update=False
	if request.method =="POST":
		form  = ScheduleForm(request.POST)
	else:
		form  = ScheduleForm()
	return save_schedule_form(request, update, pk, form, 'backoffice/partial_schedule_create.html')
	
def update_schedule(request, pk):
	update=True
	schedule = get_object_or_404(Schedule, id=pk)
	if request.method =='POST':
		form = ScheduleForm(request.POST, instance=schedule)
	else:
		form = ScheduleForm(instance=schedule)
	return save_schedule_form(request, update, pk, form, 'backoffice/partial_schedule_update.html')	

def schedule_delete(request, pk):
	schedule = get_object_or_404(Schedule, id=pk)

	data = dict()
	if request.method == "POST":
		schedule.appointment.status  = 'pending'
		schedule.appointment.save()
		schedule.delete()
		data['form_is_valid']  = "True"
		appointments = Appointment.objects.all()
		data['html_book_list'] = render_to_string('backoffice/partial_appointment_list.html', {
			'appointments':appointments})
	else:
		context           = {'schedule':schedule}
		data['html_form'] =	render_to_string('backoffice/partial_schedule_delete.html',
			context, request=request,
			)	 
	return JsonResponse(data)	

def list(request):
	appointments = Appointment.objects.all()
	for a in appointments:
		print(a.doctor)
	return render(request, 'backoffice/appointment-list.html', {'appointments':appointments})


def detail(request, id):
	appointment = get_object_or_404(Appointment, id=id)
	pass

def forma(request):
	return render(request, 'appointment-4.html')


def step1(request):
	print(request.POST)
	initial={'fn':request.session.get('fn', None)}
	form   = AppointmentForm(request.POST or None, initial=initial)
	if request.method =='POST':
		request.session['fn'] = form.cleaned_data['fn']
		return 

def test(request):
	print('something going here')
	return render(request, 'appointment-3.html')	


def new_appointment(request):
	if request.method =='POST':
		appointment = AppointmentForm(request.POST)
		if appointment.is_valid():
			appointment = appointment.cleaned_data
			appointment.save()
	else:
		appointment = AppointmentForm()
	return render(request, 'backoffice/new-appointment.html', {'appointment':appointment})	


def all_appointments(request):
	appointments_list = Appointment.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(appointments_list,100)
	try:
		appointments = paginator.page(page)
	except PageNotAnInteger:
		appointments = paginator.page(1)
	except EmptyPage:
		appointments = paginator.page(paginator.num_pages)
	return render(request, 'backoffice/all-appointments.html', {'appointments':appointments})	


def pending_appointments(request):
	return render(request, 'backoffice/new-appointment.html')				