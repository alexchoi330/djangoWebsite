from django.urls import path
from . import views
#urls = /products or /products/1/detail , etc
#all urls start with /, 


urlpatterns = [
    path('', views.index),
    path('new', views.index1)
]
