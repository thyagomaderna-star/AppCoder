from django import forms
class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre del curso")
    camada = forms.IntegerField(label="Camada")

class BusquedaCursoFormulario(forms.Form):
    camada = forms.IntegerField(label="Camada")