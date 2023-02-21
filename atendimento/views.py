from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FormAtendimento


def agendamento(request):

    if request.method != 'POST':
        form = FormAtendimento()
        return render(request, 'agendamento.html', {'form': form})

    form = FormAtendimento(request.POST)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Agendamento cadastrado com sucesso!')

    return redirect('agendamento')


def voltarhome(request):
    return redirect('home')