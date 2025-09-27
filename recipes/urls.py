#Arquivo de URLs do APP Receitas

from django.urls import path
from . import views #Importanto a view

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"), # Home
    path('recipes/<int:id>/', views.recipe, name="recipe"), #Detalhes da Recipe
]