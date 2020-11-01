from django.contrib import admin
from .models import Page, PageCategory
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(PageCategory)
class PageCategory(admin.ModelAdmin):
	list_display = ('category_name', 'category_description')

@admin.register(Page)
class PagesAdmin(admin.ModelAdmin):
	list_display  =('title', 'slug', 'page_category', 'priority', 'author',  'created_at', 'updated_at', 'status')
	prepopulated_fields = {'slug':('title',)}
	list_filter   = ('status', 'created_at', 'author')
	search_fields = ('title', 'body')

	allow_tags    = True

	def body(self, obj):
		return mark_safe(obj)

	def save_model(self, request, obj, form, change):
		obj.body=mark_safe(obj.body)
		super().save_model(request, obj, form, change)
