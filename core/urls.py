from django.urls import path
from .views import cadastro,logado,plataforma,desloga


urlpatterns = [
    path('',cadastro,name='cadastro'),
    path('log',logado,name='logando'),
    path('pla',plataforma),
    path('des',desloga,name='deslog')
]