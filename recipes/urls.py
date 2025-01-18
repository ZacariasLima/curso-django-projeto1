#Arquivo de URLs do APP Receitas

from django.urls import path
from . import views #Importanto a view

urlpatterns = [
    path('', views.home), # Home
    path('recipes/<int:id>/', views.recipe), #Detalhes da Recipe
]