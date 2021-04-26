from django.shortcuts import render
from .models import Blog

# Create your views here.


def home(request):
    return render(request,'shop_project/home.html',{})


def list_blog(request):

    blogs = Blog.objects.all()

    return render(request,'shop_project/list_blog.html',{'blogs':blogs})