from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models

#criação das tabelas (banco de dados)

class Contato(models.Model):
        email = models.EmailField(help_text='exemplo@email.com', unique=True)
        telefone = models.CharField(
            max_length=15,
            unique= True,
            validators=[
                RegexValidator(regex=r'^\d{10,15}$', message='O número de telefone deve conter apenas dígitos.')]
        )
        cidade = models.CharField(max_length=80)
        endereco = models.CharField(max_length=50)
        numero = models.IntegerField()

        def __str__(self):
            return self.email

class Pessoa(models.Model):
        nome = models.CharField(max_length=100, help_text='nome completo')
        data_nascimento = models.DateField()
        GENEROS = [
            ('Masculino', 'Masculino'),
            ('Feminino', 'Feminino'),
            ('Não-binário', 'Não-binário'),
            ('Outro', 'Outro'),
            ('Prefiro não dizer', 'Prefiro não dizer'),
        ]
        genero = models.CharField(max_length=20, choices=GENEROS)
        criado_em = models.DateTimeField(auto_now_add=True)
        contato = models.OneToOneField(Contato, on_delete=models.CASCADE, related_name='pessoa')


        def __str__(self):
            return self.nome

class Experiencia(models.Model):
        empresa = models.CharField(max_length=50)
        cargo = models.CharField(max_length=50)
        duracao = models.CharField(max_length=20)
        resumo = models.TextField(max_length=1000)
        pessoa = models.ManyToManyField(Pessoa, related_name='experiencias')


        def __str__(self):
            return self.empresa




class Formacao(models.Model):
        instituicao = models.CharField(max_length=50)
        curso = models.CharField(max_length=50)
        periodo = models.CharField(max_length=50)
        pessoa = models.ManyToManyField(Pessoa, related_name='formacoes')

        def __str__(self):
            return self.instituicao

