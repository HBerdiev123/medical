from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Category
from .forms import CommentForm
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.db.models import Count



# Create your views here.

def list(request, tag_slug=None, cat_slug=None):
	object_list = Post.objects.all()
	section = 'blog'
	tag = None

	if cat_slug:
		cat = get_object_or_404(Category, slug=cat_slug)
		object_list = object_list.filter(post_category=cat)

	if tag_slug:
		tag   = get_object_or_404(Tag, slug=tag_slug)
		object_list = object_list.filter(tags__in=[tag])

	page = request.GET.get('page')
	paginator = Paginator(object_list, 1)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'blog.html', {'posts':posts, 'page':page, 'tag':tag})


def detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	comments = post.comments.filter(active=True)
	
	post_tag_ids = post.tags.values_list('id', flat=True)
	similar_posts= Post.published.filter(tags__in=post_tag_ids).exclude(id=post.id)
	similar_posts= similar_posts.annotate(same_tags=Count('tags'))\
	.order_by('-same_tags', '-publish')[:3]
	new_comment=None

	if request.method=='POST':
		comment_form=CommentForm(data=request.POST)
		# print(request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post=post
			new_comment.save()

	else:
		comment_form = CommentForm()	

	return render(request, 'blog-detail.html', {'post':post, 
		'comments':comments, 
		'new_comment':new_comment,
		'comment_form':comment_form,
		'similar_posts':similar_posts})	


def create_comment(request):
	form = CommentForm()
	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid():
			comment.cleaned_data
			comment.save()
		
	return render(request, 'blog-detail.html',{'form':form})	

# def prev_next_post():
# 	posts = Post.objects.reverse()
# 	prev_item = posts[0]
# 	next_item =	post[1]
# 	return {'prev': prev_item, 'next_item':next_item}