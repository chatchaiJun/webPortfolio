from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from bs4 import BeautifulSoup
from django.db.models import Q

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
    return render(request,'blogapp/article.html',{'posts':posts})