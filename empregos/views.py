from django.shortcuts import render
from .models import Vaga, Candidato
from .forms import CandidatoForm, VagaForm

# Create your views here.

def index(request):
    return render(request, 'empregos/index.html')

def candidatos(request):
    candidatos = Candidato.objects.all()
    dados = {
        'candidatos': candidatos,
    }
    return render(request, 'empregos/lista_candidatos.html', dados)

def vagas(request):
    vagas = Vaga.objects.all()
    dados = {
        'vagas': vagas,
    }
    return render(request, 'empregos/lista_vagas.html', dados)

def detalhe_vaga(request, vaga_nome):
    vaga = Vaga.objects.get(nome=vaga_nome)
    dados = {
        'vaga': vaga,
    }
    return render(request, 'empregos/detalhe_vaga.html', dados)

def detalhe_candidato(request, candidato_nome):
    candidato = Candidato.objects.get(nome=candidato_nome)
    dados = {
        'candidato': candidato,
    }
    return render(request, 'empregos/detalhe_candidato.html', dados)

def cadastrar_vaga(request):
    form = VagaForm() 
    dados = {
        'form': form,
    }
    return render(request, 'empregos/cadastrar_vaga.html', dados)   

def cadastrar_candidato(request):
    form = CandidatoForm()
    dados = {
        'form': form,
    }
    return render(request, 'empregos/cadastrar_candidato.html', dados)
