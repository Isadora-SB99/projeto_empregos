from django.shortcuts import render, get_object_or_404, redirect
from .models import Vaga, Candidato
from .forms import VagaForm, CandidatoForm

def index(request):
    return render(request, 'empregos/index.html')

def vagas(request):
    vagas = Vaga.objects.all()
    return render(request, 'empregos/lista_vagas.html', {'vagas': vagas})

def detalhe_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    return render(request, 'empregos/detalhe_vaga.html', {'vaga': vaga})

def candidatos(request):
    candidatos = Candidato.objects.select_related('vaga').all()
    return render(request, 'empregos/lista_candidatos.html', {'candidatos': candidatos})

def detalhe_candidato(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    return render(request, 'empregos/detalhe_candidato.html', {'candidato': candidato})

def cadastrar_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vagas')
    else:
        form = VagaForm()
    return render(request, 'empregos/cadastrar_vaga.html', {'form': form})

def cadastrar_candidato(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidatos')
    else:
        form = CandidatoForm()
    return render(request, 'empregos/cadastrar_candidato.html', {'form': form})
