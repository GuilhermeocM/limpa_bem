from django.shortcuts import redirect, render
from .models import FormCliente

def cadastro(request):
    if request.method != 'POST':
        form = FormCliente()
        return render(request, 'cadastro.html', {'form': form})

    form = FormCliente(request.POST)
    if form.is_valid():
        form.save()

    return redirect('agendamento')