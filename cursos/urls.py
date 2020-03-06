from django.urls import path

from .views import AvaliacaoAPIView, AvaliacoesAPIView, CursoAPIView, CursosAPIView, UsuarioAPIView, UsuariosAPIView

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacao'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='curso_avaliacao_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),

    path('usuarios/', UsuarioAPIView.as_view(), name='usuarios'),
    path('usuarios/<int:pk>/', UsuariosAPIView.as_view(), name='usuario'),
]