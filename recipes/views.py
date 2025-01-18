from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Functions que chamam as páginas
def home (request):
    return render (request, 'recipes/pages/home.html', context= {
        'name': 'Zacarias Figueiredo Lima'
    })

def recipe (request, id):
    return render (request, 'recipes/pages/home.html', context= {
        'name': 'Zacarias Figueiredo Lima'
    })