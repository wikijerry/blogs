from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
#from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class BlogView(ListView):#this is to view content in list
    model = Post
    template_name = 'blogs_app/home.html'

class BlogDetailView(DetailView):#single content
    model = Post
    template_name = "blogs_app/post_details.html"

class CreateView(CreateView):
    model = Post
    template_name = "blogs_app/post_new.html"
    fields='__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blogs_app/post_edit.html"
    fields=['title','body','img']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blogs_app/post_delete.html"
    success_url= reverse_lazy('BlogView')


