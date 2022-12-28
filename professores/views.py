import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Professor
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


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

        return HttpResponse('testando')


def attProf(request):
    idProf = request.POST.get('idProf')
    professor = Professor.objects.filter(id=idProf)
    profJson = json.loads(serializers.serialize(
        'json', professor))[0]['fields']
    profIdJson = json.loads(serializers.serialize('json', professor))[0]['pk']
    data = {'professor': profJson, 'profIdJson': profIdJson}
    return JsonResponse(data)

@csrf_exempt
def updateProf(request, id):
    data = json.loads(request.body)

    nome = data['nome']
    nomeSocial = data['nomeSocial']
    cpf = data['cpf']

    professor = get_object_or_404(Professor, id=id)
    try:
        professor.nome = nome
        professor.nomeSocial = nomeSocial
        professor.cpf = cpf
        professor.save()
        return JsonResponse({'status': '200', 'nome': nome, nomeSocial:'nomeSocial', 'cpf': cpf})
    except:
        return JsonResponse({'status': '500'})
