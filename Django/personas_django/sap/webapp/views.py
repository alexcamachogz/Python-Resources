# Create your views here.
from django.shortcuts import render
from personas.models import Persona


def bienvenido(request):
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')

    elementos = {
        'no_personas': no_personas,
        'personas': personas
    }

    return render(request, 'bienvenido.html', elementos)