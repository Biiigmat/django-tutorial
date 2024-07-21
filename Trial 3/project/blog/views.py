from django.shortcuts import render
from django.http import HttpResponse

def home_page (request):
    return render (request , 'blog/index.html')

def about_page(request):
    return render (request , 'blog/about.html')

def contact_page(request):
    return render (request , 'blog/contact.html')

def blogsingle_page(request):
    return render (request , 'blog/blog-single.html')

def bloghome_page(request):
    return render (request , 'blog/blog-home.html')

def elements_page(request):
    return render (request , 'blog/elements.html')