# Author : Animesh Agrawal
# Date : 30-09-2022

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('hello')

def about(request):
    return HttpResponse('about')

def navigator(request):
    return HttpResponse('<a href="https://www.facebook.com">facebook</a> <br> <a href="https://www.instagram.com">instagram</a>')

def textutils(request):
    params={'name':'animesh','place':'chaand'}
    return render(request,'index.html',params)