from django.urls import path
from .views import index,cadastro,logado,plataforma,desloga,mudar_senha



urlpatterns = [
    path('in',index,name='index'),
    path('cad',cadastro,name='cadastro'),
    path('log',logado,name='logando'),
    path('pla',plataforma,name='plata'),
    path('des',desloga,name='deslog'),
    path('muda',mudar_senha,name='muda'),

]