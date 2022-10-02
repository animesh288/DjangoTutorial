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

def textutils2(request):
    return render(request,'index2.html')

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    if removepunc=='on':
        analyzed_text=''
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punc:
                analyzed_text+=char
        params={'purpose':'remove punctuations','analyzed_text':analyzed_text}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse('Error')
