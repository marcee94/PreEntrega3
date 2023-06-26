from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from Oncoliq.models import *
from Oncoliq.forms import *

def inicio(request):
    return render (request,"Oncoliq/inicio.html")

def laboratorio(request):
    return render (request,"Oncoliq/laboratorio/laboratorio.html")

def medico(request):
    return render (request, "Oncoliq/medico/medico.html")

def paciente(request):
    return render (request, "Oncoliq/paciente/paciente.html")

def setLaboratorio(request):
    if request.method == 'POST':
        miFormulario = formSetLaboratorio(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            laboratorio = Laboratorio(laboratorio=data["laboratorio"],operario=data["operario"],email=data["email"],equipo=data["equipo"],fecha=data["fecha"],resultado=data["resultado"])
            laboratorio.save()
            return render(request,"Oncoliq/inicio.html")
    else:
        miFormulario = formSetLaboratorio()

    return render(request,"Oncoliq/laboratorio/setLaboratorio.html",{"miFormulario":miFormulario})

def getLaboratorio(request):
    return render (request, "Oncoliq/laboratorio/getLaboratorio.html")

def buscarLaboratorio(request):
    if request.GET["operario"]:
        operario = request.GET["operario"]
        operario = Laboratorio.objects.filter(operario = operario)
        return render(request,"Oncoliq/laboratorio/getLaboratorio.html",{"operario":operario})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

def setMedico(request):
    if request.method == 'POST':
        miForm = formSetMedico(request.POST)
        print(miForm)
        if miForm.is_valid:
            data2 = miForm.cleaned_data
            medico = Medico(nombre=data2["nombre"],apellido=data2["apellido"],email=data2["email"],institucion=data2["institucion"],informe=data2["informe"],mamografia=data2["mamografia"])
            medico.save()
            return render(request,"Oncoliq/inicio.html")
    else:
        miForm = formSetMedico()

    return render(request,"Oncoliq/medico/setMedico.html",{"miForm":miForm})

def getMedico(request):
    return render (request, "Oncoliq/medico/getMedico.html")

def buscarMedico(request):
    if request.GET["email"]:
        email = request.GET["email"]
        email = Medico.objects.filter(email = email)
        return render(request,"Oncoliq/medico/getMedico.html",{"email":email})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

def setPaciente(request):
    if request.method == 'POST':
        miForm2 = formSetPaciente(request.POST)
        print(miForm2)
        if miForm2.is_valid:
            data3 = miForm2.cleaned_data
            paciente = Paciente(nombre=data3["nombre"],apellido=data3["apellido"],email=data3["email"])
            paciente.save()
            return render(request,"Oncoliq/inicio.html")
    else:
        miForm2 = formSetPaciente()

    return render(request,"Oncoliq/paciente/setPaciente.html",{"miForm2":miForm2})

def getPaciente(request):
    return render (request, "Oncoliq/paciente/getPaciente.html")

def buscarPaciente(request):
    if request.GET["email"]:
        email = request.GET["email"]
        email = Paciente.objects.filter(email = email)
        return render(request,"Oncoliq/paciente/getPaciente.html",{"email":email})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)