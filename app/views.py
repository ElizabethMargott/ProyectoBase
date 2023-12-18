from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404

def saludo(req):
    return HttpResponse("Hello World!")

def home(req):
    context = {}
    return render(req, 'home.html', context)

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    
    return render(request, 'crear_proyecto.html', {'form': form})

def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)

    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto})

def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
        
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
        return redirect('detalle_proyecto', proyecto_id=proyecto_id)
    else:
        form = ProyectoForm(instance=proyecto)
        
    return render(request, 'editar_proyecto.html', {'form': form, 'proyecto': proyecto})

def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id) 
    
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')

    return render(request, 'eliminar_proyecto.html', {'proyecto': proyecto})
