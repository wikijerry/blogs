from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('signup/',SignupView.as_view(),name='signup'),
]
