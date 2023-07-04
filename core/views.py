from django.shortcuts import render
from .models import Produto, Cliente
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader


def index(request):
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()
    # print(dir(request.user))

    print(f" User: {request.user}")

    if str(request.user == 'AnonymousUser'):
        teste = 'Usuario não logado'
    else:
        teste = 'Usuario logado'

    context = {
        'logado': teste,
        'produtos': produtos,
        'cliente': clientes

    }

    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request,id):
    # prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('400.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

























