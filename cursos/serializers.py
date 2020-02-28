from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializers(serializers.ModelSerializer):

    class Meta:

        extra_kwargs = {
            'email':{
                'write_only': True
            }
        }

        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'ativo'
        )

class CursoSerializers(serializers.ModelSerializer):

    class Meta:

        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        )