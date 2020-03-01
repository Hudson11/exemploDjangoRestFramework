from rest_framework import generics

from .models import Curso, Avaliacao, Usuario
from .serializers import CursoSerializers, AvaliacaoSerializers, UsuarioSerializers

#ListCreatedAPIView -> GET / POST
class CursosAPIView (generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

#RetrieveUpdateDestroyAPIView PUT / DELETE / GETByID
class CursoAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

class AvaliacoesAPIView (generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers

class AvaliacaoAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers

class UsuarioAPIView (generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers

class UsuariosAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers
