"""
URL configuration for agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home , name='home'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('consultar_cliente/',views.consultar_cliente, name='consultar_cliente'),
    path('ver_cliente/<int:id>',views.ver_cliente, name='ver_cliente'),
    path('deletar_cliente/<int:id>',views.deletar_cliente, name='deletar_cliente'),
    path('cadastrar_servico/', views.cadastrar_servico, name='cadastrar_servico'),
    path('agendamento/', views.consultar_agendamento, name='agendamento'),
    path('agendar_servico/', views.agendar_servico, name='agendar_servico'),
    path('ver_agendamento/<int:id>', views.ver_agendamento, name='ver_agendamento'),
    path('relatorio_agendamento/', views.relatorio_agendamento, name='relatorio_agendamento'),

]
