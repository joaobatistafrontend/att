from django.urls import path
from .views import plataforma
from .views import Cadastro,Logado,Desloga,Index,Senha


urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('cadastra',Cadastro.as_view(),name='cadastro'),
    path('login/',Logado.as_view(),name='logando'),
    path('desloga/',Desloga.as_view(),name='deslog'),
    path('plataforma/',plataforma,name='pla'),
    path('mudasenha',Senha.as_view(),name='muda')
]