from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def professores(request):
    if request.method == "GET":
        return render(request, 'professores.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        nomeSocial = request.POST.get('nomeSocial')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        senhaConfirm = request.POST.get('senhaConfirm')
        aniversario = request.POST.get('aniversario')

        print(nome)

        return HttpResponse('teste')