from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
# request to /products then call index function

def index(request):
    products = Product.objects.all()
    #.filter() to filer
    #.save() to save existing one
    return render(request, 'index.html', {'products': products})


def index1(request):
    return HttpResponse("this is the new page")
