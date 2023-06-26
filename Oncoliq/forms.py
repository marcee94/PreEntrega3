from django import forms

class formSetLaboratorio (forms.Form):
    laboratorio = forms.CharField(max_length=30)
    operario = forms.CharField(max_length=30)
    email = forms.EmailField()
    equipo = forms.CharField(max_length=30)
    fecha = forms.DateField()
    resultado = forms.CharField(max_length=30)

class formSetMedico (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    institucion = forms.CharField(max_length=30)
    informe = forms.CharField(max_length=200)
    mamografia = forms.CharField(max_length=30)

class formSetPaciente(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()