from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vagas/', views.vagas, name='vagas'),
    path('candidatos/', views.candidatos, name='candidatos'),
    path('cadastrar_vaga/', views.cadastrar_vaga, name='cadastrar_vaga'),
    path('cadastrar_candidato/', views.cadastrar_candidato, name='cadastrar_candidato'),

]
