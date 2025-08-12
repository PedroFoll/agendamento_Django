from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from .models import Usuario, Servico, Agendamento
limit=5
limite=10
pagina=1
# Create your views here.

def home(request):
    return render(request, 'home.html', {})
    
def cadastrar_usuario(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_usuario.html', {})
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        tipo_usuario = request.POST.get('tipo_usuario', 'cliente')
          
        user = Usuario(nome=nome,email=email, telefone=telefone, endereco=endereco,tipo_usuario=tipo_usuario)
        user.save()
        return redirect('/cadastrar_usuario/')
    
def consultar_cliente(request):
    nome_filtrar=request.GET.get('nome_filtrar')
    email_filtrar=request.GET.get('email_filtrar')
    tipo_usuario_filtrar= request.GET.get('tipo_usuario_filtrar')

    clientes = Usuario.objects.all()

    if nome_filtrar:
        clientes = clientes.filter(nome__contains=nome_filtrar)
    
    if email_filtrar:
        clientes = clientes.filter(email__contains=email_filtrar)
    
    if tipo_usuario_filtrar:
        clientes = clientes.filter(tipo_usuario__iexact=tipo_usuario_filtrar.lower())


    return render(request, 'consultar_cliente.html', {'clientes': clientes})

def ver_cliente(request,id):
    cliente=Usuario.objects.get(id=id)
    return  render(request, 'ver_clientes.html', {'cliente': cliente})

def deletar_cliente(request,id):
    cliente=Usuario.objects.get(id=id)
    cliente.delete()
    return redirect('/consultar_cliente/')

def cadastrar_servico(request):
   
    if request.method == 'GET':
        return render(request, 'cadastro_Servico.html',{})
    else:
        nome_servico = request.POST.get('nome_servico')
        descricao_servico = request.POST.get('descricao_servico')  
        preco_servico = request.POST.get('preco_servico')
        servico=Servico(servico=nome_servico, descricao=descricao_servico, preco=preco_servico)
        servico.save()
        return redirect('/cadastrar_servico/') 

def consultar_agendamento(request):
    clientes = Usuario.objects.all()
    servicos = Servico.objects.all()
    global pagina
    global limit
    offset = 0
    agendamentos = Agendamento.objects.all()
    qtd_agendamentos = agendamentos.count()
    agendamentos = agendamentos.order_by('data_hora')[offset:offset+limit]
    
    if 'next' in request.GET:
        pagina += 1
    elif 'back' in request.GET and pagina > 1:
        pagina -= 1
    
    
    agendamentos = Agendamento.objects.all().order_by('data_hora')[offset:offset+limit]
   
    
    return render(request, 'agendamento.html', {'clientes': clientes, 'servicos': servicos, 
                                                'agendamentos': agendamentos, 'qtd_agendamentos': qtd_agendamentos})

def agendar_servico(request):
    if request.method == 'GET':
         return render(request, 'agendamento.html', {})

    else:
        cliente_ID = request.POST.get('cliente')
        funcionario_ID = request.POST.get('funcionario')
        servico_ID = request.POST.get('servico')
        status = request.POST.get('status_filtrar')
        data_hora = request.POST.get('data_hora')

        clientes = Usuario.objects.get(pk=cliente_ID)
        servicos = Servico.objects.get(pk=servico_ID)
        funcionarios = Usuario.objects.get(pk=funcionario_ID)

        agendamento = Agendamento(cliente=clientes, funcionario=funcionarios, servico=servicos, status=status, data_hora=data_hora)
        agendamento.save()        

        return redirect('/agendamento/')

def ver_agendamento(request, id):
    agendamento = Agendamento.objects.get(id=id)
    return render(request, 'ver_agendamento.html', {'agendamento': agendamento})

def relatorio_agendamento(request):
    global pagina
    global limit
    offset = 0
    agendamentos = Agendamento.objects.all()
    qtd_agendamentos = agendamentos.count()
    selecionar_status = request.GET.get('selecionar_status')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    
    
    if selecionar_status:       
        agendamentos = agendamentos.filter(status__iexact=selecionar_status.lower())
    
    if data_inicio and data_fim:
        agendamentos = agendamentos.filter(data_hora__range=[data_inicio, data_fim])        

    if 'next' in request.GET:
        pagina += 1
    elif 'back' in request.GET and pagina > 1:
        pagina -= 1

    agendamentos =agendamentos.order_by('data_hora')[offset:offset+limit]
    offset = (pagina - 1) * limit
    qtd_agendamentos = Agendamento.objects.count()
    return render(request, 'relatorio.html', {'agendamentos': agendamentos, 'qtd_agendamentos': qtd_agendamentos})