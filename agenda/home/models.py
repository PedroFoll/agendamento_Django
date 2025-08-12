from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=20, default='Cliente')
    
    def __str__(self):
        return self.nome


class Servico(models.Model):
    servico = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    cliente = models.ForeignKey(Usuario, to_field='id', on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, to_field='id', on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Usuario, to_field='id', on_delete=models.CASCADE, related_name='funcionario_agendamento',null=True, blank=True)
    status = models.CharField(max_length=20, default='Agendado')
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"{self.cliente} - {self.servico}"