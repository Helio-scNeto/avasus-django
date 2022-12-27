import json
import re
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Professor
from django.core import serializers

def Professores(request):
    if request.method == "GET":
        profList = Professor.objects.all()
        return render(request, 'professores.html', {'professores': profList})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        nomeSocial = request.POST.get('nomeSocial')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        aniversario = request.POST.get('aniversario')

        professor = Professor.objects.filter(cpf=cpf)

        if professor.exists():
            return render(request, 'professores.html', {'nome': nome, 'nomeSocial': nomeSocial, 'estado': estado, 'cidade': cidade, 'cpf': cpf})

        professor = Professor(
            nome=nome,
            nomeSocial=nomeSocial,
            estado=estado,
            cidade=cidade,
            cpf=cpf,
            senha=senha,
            aniversario=aniversario
        )

        professor.save()

        # return HttpResponse('teste')


def attProf(request):
    idProf = request.POST.get('idProf')
    professor = Professor.objects.filter(id=idProf)
    jsonProf = json.loads(serializers.serialize('json', professor))[0]['fields']
    return JsonResponse(jsonProf)
