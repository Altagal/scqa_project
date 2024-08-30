from datetime import timezone
from django.utils import timezone
from django.db import transaction
from django.shortcuts import render, redirect

from gestao.form import RegistroEntradaForm, EntradaAmostraForm
from gestao.models import EntradaAmostra

"""
def foo_list(request):
    pre_context = {
        "card_title": "Foos",
    }
    
    context = {
    }
   
    return render(request, 'foo.html', {**pre_context, **context})

def foo_create(request):
    pre_context = {
        "card_title": "Novo Foo",
    }

    if request.method == 'GET':
        context = {
            "form": FooForm(),
        }

    if request.method == 'POST':
        form = FooForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.scqa_save(request)
            return redirect('foo_list')
        else:
            context = {
                "form": form,
            }

    return render(request, 'gestao/foo.html', {**pre_context, **context})


"""


def registro_entrada_list(request):
    pre_context = {
        "card_title": "Registros de Entrada",
    }
    registro_entrada_list = []

    context = {
        "registro_entrada_list": registro_entrada_list,
    }

    return render(request, 'gestao/registro_entrada_list.html', {**pre_context, **context})


def registro_entrada_create(request):
    pre_context = {
        "card_title": "Novo Registro de Entrada",
    }

    if request.method == 'GET':
        context = {
            "form": RegistroEntradaForm(),
            "entrada_amostra_form": EntradaAmostraForm(),
        }

    if request.method == 'POST':
        form = RegistroEntradaForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.scqa_save(request)

            for tipo_amostra, nao_conformidade in zip(request.POST.getlist("tipo_amostra"), request.POST.getlist("nao_conformidade")):
                entrada_amostra_obj = EntradaAmostra(registro_entrada_pk=obj.id, tipo_amostra=tipo_amostra, nao_conformidade=nao_conformidade)
                entrada_amostra_obj.modified_at = timezone.now
                entrada_amostra_obj.save()
        else:
            context = {
                "form": form,
            }

    return render(request, 'gestao/registro_entrada.html', {**pre_context, **context})
