from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse
import operator

def whoami(requests):
        return HttpResponse('I am Anudeep Boini , My mail is openit7anudeep@gmail.com')
def name(requests):
        return HttpResponse('My name is anudeep')
