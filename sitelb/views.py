from django.shortcuts import render

def home(request):
    return render(request, 'paginas/home.html')



def intranet(request):
    return render(request, 'paginas/intranet.html')



def cadastro(request):
    return render(request, 'paginas/cadastro.html')