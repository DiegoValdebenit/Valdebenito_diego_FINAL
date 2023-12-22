from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inscrito, Institucion
from .serializers import InscritoSerializer, InstitucionSerializer
from rest_framework.decorators import api_view
from django.views import View
from .forms import InscritoForm, InstitucionForm
from django.http import HttpResponseRedirect
from django.urls import reverse

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html') 

class AlumnoAPIView(APIView):
    def get(self, request):
        alumno = {
            "nombre": "Diego Andrés Valdebenito Oporto",
            "edad": 21,
            "institución": "INACAP",
            "carrera": "Ingeniería en Informática",
            "seccion": "IEI170",
        }
        return Response(alumno)


class Listado_Inscritos(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Ingresar_participante_View(View):
    def get(self, request):
        form = InscritoForm()
        return render(request, 'ingresar_participantes.html', {'form': form})

    def post(self, request):
        form = InscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'ingresar_participantes.html', {'form': form})

class Detalle_InscritoView(APIView):
    def get_object(self, pk):
        try:
            return Inscrito.objects.get(pk=pk)
        except Inscrito.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        inscrito = self.get_object(pk)
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)

    def put(self, request, pk):
        inscrito = self.get_object(pk)
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscrito = self.get_object(pk)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def listado_instituciones(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def ingresar_institucion(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InstitucionForm()

    return render(request, 'ingresar_institucion.html', {'form': form})


@api_view(['GET', 'PUT'])
def detalle_institucion_view(request, pk):
    def get_object(pk):
        try:
            return Institucion.objects.get(pk=pk)
        except Institucion.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    if request.method == 'GET':
        institucion = get_object(pk)
        serializer = InstitucionSerializer(institucion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        institucion = get_object(pk)
        serializer = InstitucionSerializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

