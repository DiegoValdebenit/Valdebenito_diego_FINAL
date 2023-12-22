"""
URL configuration for valdebenito_diego_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from seminario import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ingresar_participante/', views.Ingresar_participante_View.as_view(), name='ingresar_participante'),
    path('inscritos/', views.Listado_Inscritos.as_view(), name='lista_inscritos'),
    path('inscritos/<int:pk>/', views.Detalle_InscritoView.as_view(), name='detalle_inscrito'),

    path('ingresar_institucion/', views.ingresar_institucion, name='ingresar_institucion'),
    path('instituciones/', views.listado_instituciones, name='lista_instituciones'),
    path('instituciones/<int:pk>/', views.detalle_institucion_view, name='detalle_institucion'),

    path('alumno_api/', views.AlumnoAPIView.as_view(), name='alumno_api'),
]
