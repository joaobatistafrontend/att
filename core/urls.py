from django.urls import path
from .views import plataforma
from .views import Cadastro,Logado,Desloga


urlpatterns = [
    path('',Cadastro.as_view(),name='cadastro'),
    path('log/',Logado.as_view(),name='logando'),
    path('pla/',plataforma),
    path('des/',Desloga.as_view(),name='deslog'),
    path('pla/',plataforma,name='pla')
]