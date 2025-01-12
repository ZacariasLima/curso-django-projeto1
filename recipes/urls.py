#Arquivo de URLs do APP Receitas

from django.urls import path
from recipes.views import home, contact, about #Importanto a view

urlpatterns = [
    path('', home), # Home
    path('contato/', contact), # Contato
    path('sobre/', about), # Sobre
]