from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404

# Create your views here.
def signup(request):
    return HttpResponse('signup')

def login(request):
    return HttpResponse('login')