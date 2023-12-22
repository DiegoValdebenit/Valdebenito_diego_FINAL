from django import forms
from .models import Inscrito, Institucion
from django.core import validators

class InscritoForm(forms.ModelForm):
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten')
    ]

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
        max_length=60,
        error_messages={'max_length': 'El nombre no puede superar los 60 caracteres.'}
    )
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        validators=[validators.MinLengthValidator(9)]
    )
    estado = forms.ChoiceField(
        choices=ESTADOS,
        widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Estado'})
    )
    observacion = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Observación', 'rows': 3})
    )

    class Meta:
        model = Inscrito
        fields = ['nombre', 'telefono', 'institucion', 'estado', 'observacion'] 
        
class InstitucionForm(forms.ModelForm):
    nombre_institucion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=60,
        error_messages={'max_length': 'El nombre no puede superar los 60 caracteres.'}
    )
    class Meta:
        model = Institucion
        fields = ['nombre_institucion']