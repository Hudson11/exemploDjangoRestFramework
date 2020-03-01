from django.db import models

# ABSTRACT CLASS BASE
class Base(models.Model):

    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


# CLASS CURSO EXTENDS BASE
class Curso(Base):

    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo


# CLASS AVALIACAO EXTENDS BASE
class Avaliacao(Base):

    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'

class Usuario(Base):

    nome = models.CharField(unique=True, max_length=255, default='')
    email = models.EmailField()
    cpf = models.DecimalField(unique=True, max_digits=11, decimal_places=0)
    urlCurriculo = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.nome
