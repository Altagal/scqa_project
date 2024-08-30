from django.shortcuts import render

def home(request):
    pre_context={

    }

    context={

    }
    return render(request, 'home/home.html', {**pre_context, **context})
