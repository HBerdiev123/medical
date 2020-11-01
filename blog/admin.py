from django.contrib import admin
from .models import Post, Comment, Contact, Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish','status')
	list_filter  = ('status', 'created', 'publish', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields  = ('author',)
	date_hierarchy = 'publish'
	ordering       = ['status', 'publish']

admin.site.register(Post, PostAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_name', 'category_description')
	prepopulated_fields ={'slug':('category_name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'email', 'post', 'created', 'active')
	list_filter  = ('active', 'created', 'updated')
	search_field = ('author', 'email', 'body')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'subject', 'created_at')
	list_filter  = ('created_at', 'updated_at')
	search_field = ('name', 'email', 'message')
