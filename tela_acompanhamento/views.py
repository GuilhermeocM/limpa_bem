from django.shortcuts import render, redirect
from funcionario.models import Funcionario
from atendimento.models import Atendimento


def acompanhamento(request):
    atendentes = Funcionario.objects.filter(cargo="atendente")
    return render(request, 'acompanhamento.html', {
    'atendentes': atendentes,
    })
        

def voltarhome(request):
    return redirect('home')


def ver_atendimento(request, atendimentos_id):
    atendimento = Atendimento.objects.get(id=atendimentos_id)
    return render(request, 'atendimento.html', {
        'atendimento': atendimento
    })