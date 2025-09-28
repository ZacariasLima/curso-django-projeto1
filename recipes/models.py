from django.db import models
from django.contrib.auth.models import User #Usuário do Django

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=65)

    # Função para "escrita" da classe
    def __str__(self):
        return self.name

class Recipe (models.Model):
    title = models.CharField(max_length=65) #Varchar[65]
    description = models.CharField(max_length=165)
    slug = models.SlugField() #Ver depois
    preparation_time = models.IntegerField()
    description_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField() #Campo de texto sem limite
    preparation_steps_is_html = models.BooleanField(default=False) #determinação de default
    created_at = models.DateTimeField(auto_now_add=True) #Na criação preenche com sysdate
    updated_at = models.DateTimeField(auto_now=True) #No update preenche com sysdate
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    # Função para "escrita" da classe
    def __str__(self):
        return ("["+self.category.__str__()+"] "+self.title)