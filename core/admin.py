from django.contrib import admin
from .models import Curriculo

@admin.register(Curriculo)
class CurriculoAdm(admin.ModelAdmin):
    list_display = ['nome_completo','email','telefone','empresa','cargo']