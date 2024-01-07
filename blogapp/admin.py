from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog
# Register your models here.
# admin.site.register(Blog)

class BlogAdmin(SummernoteModelAdmin):
    '''Register model by BlogAdmin'''
    list_display = ('title','post','date_created','date_updated','category')
    summernote_fields = '__all__'

admin.site.register(Blog,BlogAdmin)