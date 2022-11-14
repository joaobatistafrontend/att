from django.urls import path
<<<<<<< HEAD
from .views import plataforma
from .views import Cadastro,Logado,Desloga


urlpatterns = [
    path('',Cadastro.as_view(),name='cadastro'),
    path('log/',Logado.as_view(),name='logando'),
    path('pla/',plataforma),
    path('des/',Desloga.as_view(),name='deslog'),
    path('pla/',plataforma,name='pla')
=======
from .views import index,cadastro,logado,plataforma,desloga,mudar_senha



urlpatterns = [
    path('in',index,name='index'),
    path('cad',cadastro,name='cadastro'),
    path('log',logado,name='logando'),
    path('pla',plataforma,name='plata'),
    path('des',desloga,name='deslog'),
    path('muda',mudar_senha,name='muda'),

>>>>>>> 0b52a9afecd2d3cddf1fd4406e4889788c895810
]