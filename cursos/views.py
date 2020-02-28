from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializers, AvaliacaoSerializers

class CursoAPIView(APIView):
    '''
    API DE ENSINO UDEMY
    '''

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializers(cursos, many = True)
        return Response(serializer.data)

class AvaliacaoAPIView(APIView):
    '''
    API DE AVALIAÇÕES
    '''

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializers(avaliacoes, many=True)
        return Response(serializer.data)
    