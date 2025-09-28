#Arquivo de URLs do APP Receitas

from django.urls import path
from . import views #Importanto a view

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"), # Home
    path('recipes/category/<int:category_id>/', views.category, name="category"), #Futuro filtro de cacegoria
    path('recipes/<int:id>/', views.recipe, name="recipe"), #Detalhes da Recipe
]