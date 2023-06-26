from django.urls import path
from Oncoliq.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('laboratorio/', laboratorio, name="Laboratorio"),
    path('medico/', medico, name="Medico"),
    path('paciente/', paciente, name="Paciente"),
    path('setLaboratorio/', setLaboratorio, name="setLaboratorio"),
    path('getLaboratorio/', getLaboratorio, name="getLaboratorio"),
    path('buscarLaboratorio/', buscarLaboratorio, name="buscarLaboratorio"),
    path('setMedico/', setMedico, name="setMedico"),
    path('getMedico/', getMedico, name="getMedico"),
    path('buscarMedico/', buscarMedico, name="buscarMedico"),
    path('setPaciente/', setPaciente, name="setPaciente"),
    path('getPaciente/', getPaciente, name="getPaciente"),
    path('buscarPaciente/', buscarPaciente, name="buscarPaciente"),
]