from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Project
from bs4 import BeautifulSoup
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

# Create your views here.
def style_remove(request,post):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(post, 'html.parser')
    
    # Remove inline styles from all elements
    for tag in soup.find_all(['span', 'img']):
        if 'style' in tag.attrs:
            if tag.name == 'span':
                # If the tag is a span, remove the style attribute
                del tag['style']
            elif tag.name == 'img':
                # If the tag is an img, update the style attribute to set width to 100%
                tag['style'] = 'width: 100%;'


    # Get the modified HTML content
    modified_content = str(soup)

    # Pass the modified content to the template
    context = modified_content
    return context

def home(request):
    # return HttpResponse("Django")
    posts = Blog.objects.order_by("-date_created")[:2]
    return render(request,'blogapp/home.html',{'posts':posts})

def about(request):
    return render(request,"blogapp/about.html")

def post_details(request,id):
    single_post = Blog.objects.get(pk=id)
    post_detail = style_remove(request,single_post.post)
    single_post.post = post_detail
    return render(request,'blogapp/post-details.html',{'post':single_post}) 

def article(request):
    posts = Blog.objects.all()
    paginator = Paginator(posts,9)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'blogapp/article.html',{'posts':posts,'tag':'article'})

def project(request):
    projects = Project.objects.all()
    paginator = Paginator(projects,9)
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    return render(request,'blogapp/article.html',{'projects':projects,'tag':'project'})


def get_project_pictures(request, project_id):
    project = Project.objects.get(id=project_id)
    pictures = project.pictures.all()

    picture_data = [{'image_url': picture.image.url, 'description': picture.description} for picture in pictures]

    return JsonResponse({'pictures': picture_data})