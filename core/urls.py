from django.urls import path
from .views import Cadastro,Logado,Desloga,Index,Senha,Plataforma
from .views import Criacao,Listagem

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('cadastra',Cadastro.as_view(),name='cadastro'),
    path('login/',Logado.as_view(),name='logando'),
    path('desloga/',Desloga.as_view(),name='deslog'),
    path('mudasenha',Senha.as_view(),name='muda'),
    path('plataforma/',Plataforma.as_view(),name='pla'),
    path('plataforma/criacao',Criacao.as_view(),name='criacao'),
    path('plataforma/listagem',Listagem.as_view(),name='listagem'),
]