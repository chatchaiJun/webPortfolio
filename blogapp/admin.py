from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog,Project, Picture
# Register your models here.
# admin.site.register(Blog)

class BlogAdmin(SummernoteModelAdmin):
    '''Register model by BlogAdmin'''
    list_display = ('title','post','date_created','date_updated','category')
    summernote_fields = '__all__'

class PictureInline(admin.TabularInline):
    model = Picture

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_updated','project_cover')
    inlines = [PictureInline]

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'image', 'description')

admin.site.register(Blog,BlogAdmin)