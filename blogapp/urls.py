from django.urls import path
from . import views
from django.conf import settings
from django.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('article',views.article,name='article'),
    path('project',views.project,name='project'),
    path('get_project_pictures/<int:project_id>/', views.get_project_pictures, name='get_project_pictures'),
    path('article/post-details/<int:id>',views.post_details,name='post-details')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
