from django.urls import path
from .views import home_page , about_page , contact_page , bloghome_page , blogsingle_page , elements_page

app_name='blog'

urlpatterns = [
    path("" , home_page , name='index'),
    path("about",about_page , name='about'),
    path('contact' , contact_page ,name='contact'),
    path('blog-home' , bloghome_page , name='blog-home'),
    path('blog-single' , blogsingle_page , name='blog-single'),
    path('elements' ,elements_page , name='elements'),
]
