from django.contrib import admin

from .models import Aluno, Curso

admin.site.register(Curso)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso', 'situacao')
    readonly_fields=['matricula',]

admin.site.register(Aluno, AlunoAdmin)
