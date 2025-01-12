from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Functions temp de HTML
def home (request):
    return render (request, 'recipes/home.html')

def contact (request):
    return HttpResponse ('Contato')

def about (request):
    return HttpResponse ('Sobre')