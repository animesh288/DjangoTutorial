from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    products=Product.objects.all()
    n=len(products)
    print(products)
    nSlides=n//4 +ceil((n/4)-(n//4))
    allProducts=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    # params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    params={'allprods':allProducts}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html  ')

def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("track")

def search(request):
    return HttpResponse("search")

def productView(request):
    return HttpResponse("prod")

def checkout(request):
    return HttpResponse("checkout")



