from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'read_nums', 'publish_date', 'is_public']
    fields = ['title', 'body', 'author', 'read_nums', 'category', 'is_public']
    list_filter = ['publish_date', 'is_public']
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.AdminSite.site_title = 'codingkai'
admin.AdminSite.site_header = '博客后台管理'
admin.AdminSite.index_title = '博客后台管理'

