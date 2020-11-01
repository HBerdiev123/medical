from django.shortcuts  import render, get_object_or_404
from blog.forms 	   import ContactForm
from doctors.models    import Doctor 
from django.http       import JsonResponse
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from blog.forms        import SearchForm
from blog.models       import Post
from pages.models      import Page, PageCategory
from appointment.forms import AppointmentForm
from sitetree.toolbox  import register_i18n_trees

register_i18n_trees(['main'],)

def index(request):
	doctors 	 = Doctor.objects.all()
	latest_posts = Post.published.all()[:3]
	id_slider    = get_object_or_404(PageCategory, category_name ='home-slider') 
	id_emergency = get_object_or_404(PageCategory, category_name ='home-emergency')
	id_welcome   = get_object_or_404(PageCategory, category_name ='home-welcome')
	id_speciality= get_object_or_404(PageCategory, category_name ='home-speciality')
	id_services  = get_object_or_404(PageCategory, category_name ='home-service')
	id_video     = get_object_or_404(PageCategory, category_name ='home-video')
	id_doctor    = get_object_or_404(PageCategory, category_name ='home-doctors')
	id_counter   = get_object_or_404(PageCategory, category_name ='counter')
	
	slider       = get_object_or_404(Page, page_category=id_slider)
	emergency    = get_object_or_404(Page, page_category=id_emergency)
	welcome      = get_object_or_404(Page, page_category=id_welcome)
	speciality   = get_object_or_404(Page, page_category=id_speciality)
	services     = get_object_or_404(Page, page_category=id_services)
	video        = get_object_or_404(Page, page_category=id_video)
	doctor       = get_object_or_404(Page, page_category=id_doctor)
	counter      = get_object_or_404(Page, page_category=id_counter)

	if request.method =='post':
		a_form = AppointmentForm(request.POST)
		if a_form.is_valid():
			print('Form is valid')
			a_form = a_form.cleaned_data
			a_form.save()
			# print(a_form.save())
		else:
			print('form is not valid')	
	else:
		print('GET request is detected.')
		a_form = AppointmentForm()


	return render(request, 'index-2.html',  
		{'form':a_form, 
		'doctors':doctors, 
		'posts':latest_posts,
		'slider':slider,
		'emergency':emergency,
		'welcome':welcome,
		'speciality':speciality,
		'services':services,
		'doctor':doctor,
		'video':video,
		'doctor':doctor,
		'counter':counter

		})



def contacts(request):
	new_contact = None
	print(request.method)
	if request.method =='POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			# contact_form = contact_form.cleaned_data
			contact_form.save()
		return JsonResponse({'success':'success'})	
	else:
		contact_form = ContactForm()

	# print(contact_form)	
		return render(request, 'contacts.html', {
			'new_contact':new_contact,
			'form':contact_form})




def sign_up(request):
	return render(request, 'sign-up.html')

def login(request):
	return render(request, 'login.html')

def error_404(request):
	return render(request, '404.html')	

def post_search(request):
	form = SearchForm()
	query = None
	print(request.POST)
	results = []
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			query = form.cleaned_data['query']
			search_vector = SearchVector('title', weight='A')+\
			SearchVector('body', weight='B')
			search_query  = SearchQuery(query)
			results = Post.published.annotate(search=search_vector, rank = SearchRank(search_vector, search_query))\
			.filter(search=search_query).order_by('-rank')
	return render(request, 'search_result.html', {'form':form, 'query':query, 'results':results})


	