from django.db import models

AREA_CHOICES = [
    ('I', 'Informática'),
    ('T', 'Tecnologia'),
    ('E', 'Enfermagem')
]

TIPO_CONTRATO_CHOICES = [
    ('E', 'Estágio'),
    ('C', 'CLT'),
    ('CP', 'Cooperativa'),
    ('P', 'PJ'),
]

GENERO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('NB', 'Não-binário'),
    ('O', 'Outro'),
]

ESCOLARIDADE_CHOICES = [
    ('FUN', 'Fundamental'),
    ('MED', 'Médio'),
    ('SUP', 'Superior'),
    ('POS', 'Pós-graduação'),
    ('MES', 'Mestrado'),
    ('DOC', 'Doutorado'),
]

class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    area = models.CharField(max_length=1, choices=AREA_CHOICES)
    tipo_contrato = models.CharField(max_length=2, choices=TIPO_CONTRATO_CHOICES)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    email = models.CharField(max_length=140, unique=True)
    telefone = models.CharField(max_length=11, unique=True)
    escolaridade = models.CharField(max_length=3, choices=ESCOLARIDADE_CHOICES)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, null=True, blank=True, related_name='candidatos')

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
