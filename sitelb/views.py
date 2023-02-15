from django.shortcuts import render

def home(request):
    return render(request, 'paginas/home.html')

def cadastro(request):
    return render(request, 'paginas/cadastro.html')