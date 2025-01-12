#Arquivo de URLs do APP Receitas

from django.urls import path
from recipes.views import home #Importanto a view

urlpatterns = [
    path('', home), # Home

]