from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import HttpResponse
import operator 

def home(requests):
        return render(requests,'wcount/home.html', {'name':'Anudeep'})
def about(requests):
        return render(requests,'wcount/about.html',{'userid':'BeingBoini'})
def hobbies(requests):
        return HttpResponse('<h1> Hobbies</h1><ol><li>Singing</li><li>Dancing</li></ol>')
