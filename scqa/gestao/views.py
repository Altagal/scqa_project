from django.db import transaction
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404

from gestao.form import RegistroEntradaForm, RegistroEntradaAmostraForm, RegistroEntradaExameForm
from gestao.models import RegistroEntrada, RegistroEntradaExame, RegistroEntradaAmostra

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
    registro_entrada_list = RegistroEntrada.objects.all()

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
            "entrada_form": RegistroEntradaForm(),
            "entrada_amostra_form": RegistroEntradaAmostraForm(),
            "entrada_exame_form": RegistroEntradaExameForm(),
        }

    if request.method == 'POST':
        entrada_form = RegistroEntradaForm(request.POST)
        entrada_amostra_form = RegistroEntradaAmostraForm(request.POST)
        entrada_exame_form = RegistroEntradaExameForm(request.POST)

        if entrada_form.is_valid() and entrada_amostra_form.is_valid() and entrada_exame_form.is_valid():
            with transaction.atomic():
                registro_entrada_obj = entrada_form.save(commit=False)
                registro_entrada_obj.modified_at = datetime.now()
                registro_entrada_obj.save()

                entrada_amostra_obj = entrada_amostra_form.save(commit=False)
                entrada_amostra_obj.registro_entrada_pk = registro_entrada_obj
                entrada_amostra_obj.modified_at = datetime.now()
                entrada_amostra_obj.save()

                entrada_exame_obj = entrada_exame_form.save(commit=False)
                entrada_exame_obj.registro_entrada_pk = registro_entrada_obj
                entrada_exame_obj.modified_at = datetime.now()
                entrada_exame_obj.save()

            return redirect('registro_entrada_list')

        else:
            print(entrada_form.errors)
            print(entrada_amostra_form.errors)
            print(entrada_exame_form.errors)

            context = {
                "entrada_form": entrada_form,
                "entrada_amostra_form": entrada_amostra_form,
                "entrada_exame_form": entrada_exame_form,
            }

    return render(request, 'gestao/registro_entrada.html', {**pre_context, **context})


def registro_entrada_read(request, pk):
    pre_context = {
        "card_title": "Registro de Entrada",
    }

    entrada_obj = get_object_or_404(RegistroEntrada, id=pk)
    entrada_exame_obj = RegistroEntradaExame.objects.get(registro_entrada_pk=entrada_obj.id)
    entrada_amostra_obj = RegistroEntradaAmostra.objects.get(registro_entrada_pk=entrada_obj.id)

    context = {
        "is_view": True,
        "entrada_form": RegistroEntradaForm(instance=entrada_obj, readonly=True),
        "entrada_exame_form": RegistroEntradaExameForm(instance=entrada_exame_obj, readonly=True),
        "entrada_amostra_form": RegistroEntradaAmostraForm(instance=entrada_amostra_obj, readonly=True),
    }
    return render(request, 'gestao/registro_entrada.html', {**pre_context, **context})
