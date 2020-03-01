from django.urls import path

from .views import AvaliacaoAPIView, AvaliacoesAPIView, CursoAPIView, CursosAPIView, UsuarioAPIView, UsuariosAPIView

urlpatterns = [
    #GET POST
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('usuarios/', UsuarioAPIView.as_view(), name='usuarios'),
    #PUT DELETE GETByID
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
    path('usuarios/<int:pk>/', UsuariosAPIView.as_view(), name='usuario')
]