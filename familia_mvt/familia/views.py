from multiprocessing import context
from django.shortcuts import render
from familia.models import familia_datos


# Create your views here.
def cargar_datos(request):
    nueva_familia = familia_datos.objects.create(nombre = 'Benicio', apellido = 'Gomez Salinas', parentesco = 'herman0',edad = 18, fecha_nacimiento = '1995-02-04')
    context = {
        'nueva_familia' :nueva_familia
        }
    return render(request, 'cargar_datos.html', context=context )

def list_familia(request):
    familia = familia_datos.objects.all()
    context = {
        'familia' :familia
    }
    return render(request, 'familia_lista.html', context=context)
