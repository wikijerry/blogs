from msilib.schema import ListView
from django.http import HttpResponse
from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

class BlogView(ListView):
    model = Post
    template_name = "blogs_app/home.html"

