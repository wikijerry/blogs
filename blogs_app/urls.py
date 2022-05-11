from django import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>/edit',BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_details'),
    path('post/new/', CreateView.as_view(), name='post_new'),
    path('',BlogView.as_view(),name='BlogView'),    
]

