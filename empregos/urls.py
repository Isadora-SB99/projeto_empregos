from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vagas/', views.vagas, name='vagas'),
    path('vaga/<int:pk>/', views.detalhe_vaga,     name='detalhe_vaga'),      
    path('candidatos/', views.candidatos, name='candidatos'),
    path('candidato/<int:pk>/', views.detalhe_candidato, name='detalhe_candidato'),  
    path('cadastrar_vaga/', views.cadastrar_vaga, name='cadastrar_vaga'),
    path('cadastrar_candidato/', views.cadastrar_candidato, name='cadastrar_candidato'),
]
