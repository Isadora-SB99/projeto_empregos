from django.db import models

AREA_CHOICES = [
    ('I', 'Informática'),
    ('T', 'Tecnologia'),
    ('E', 'Enfermagem')
]

TIPO_CONTRATO_CHOICES = [
    ('E', 'Estágio'),
    ('C', 'CLT'),
]

GENERO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('NB', 'Não-binário'),
    ('O', 'Outro'),
]


ESCOLARIDADE_CHOICES = [
    ('fun', 'Fundamental'),
    ('med', 'Médio'),
    ('sup', 'Superior'),
    ('pos', 'Pós-graduação'),
    ('mes', 'Mestrado'),
    ('dou', 'Doutorado'),
]


class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    area = models.CharField(max_length=100, choices=AREA_CHOICES)
    tipo_contrato = models.CharField(max_length=100, choices=TIPO_CONTRATO_CHOICES)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=30, choices=GENERO_CHOICES)
    email = models.CharField(max_length=140, unique=True)
    telefone = models.CharField(max_length=11, unique=True)
    escolaridade = models.CharField(max_length=50, choices=ESCOLARIDADE_CHOICES)

    def __str__(self):
        return self.nome
