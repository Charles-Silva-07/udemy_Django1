from django.shortcuts import render
from .models import Produto


def index(request):
    produto = Produto.objects.all()
    # print(dir(request.user))
    print(f" User: {request.user}")

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuario não logado'
    else:
        teste = 'Usuario Logado'

    context = {
        'curso': 'Curso massa que esse que eu estou fazendo',
        'logado': teste,
        'produtos': produto,
    }

    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, id):
    prod = Produto.objects.get(id=id)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)