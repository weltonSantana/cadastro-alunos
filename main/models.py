from django.db import models
from random import randint

from django.core.exceptions import ValidationError
from datetime import datetime
          

class Curso(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class Aluno(models.Model):

    VINCULO = (
        ('Ativo', 'Ativo'),
        ('Trancado', 'Trancado'),
        ('Formado', 'Formado'),
    )

    matricula = models.CharField(null=True, max_length=10, unique=True)
    nome = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    semestreInicio = models.PositiveIntegerField('Inicio do Semestre')
    semestreFim = models.PositiveIntegerField('Fim do Semestre', null=True, blank=True)
    situacao = models.CharField(
        'Situação',
        max_length=8,
        choices=VINCULO,
        default='Ativo'
    )

    
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural =  'Alunos'
        ordering = ['nome'] 
    
    

    def clean(self):
        if self.semestreFim == None:
            return self.semestreFim
        elif self.semestreFim <= self.semestreInicio:
            raise ValidationError('Não é possivel terminar o semestre antes do seu inicio!') 
        elif self.semestreFim > self.semestreInicio and self.situacao == 'Ativo':
            raise ValidationError('Não é possivel terminar o semestre e continuar ativo!') 
        elif self.semestreFim > self.semestreInicio and self.semestreFim < self.semestreInicio+4 and self.situacao == 'Formado':
            raise ValidationError('Só é possivel formar com no minimo 4 anos de graduação!') 
            
    
         

    def __str__(self):
        return self.nome 


    def save(self):
        if not self.matricula:
         self.gerarMatricula()
        

        return super().save()

    def gerarMatricula(self):
        
        self.matricula= str(self.semestreInicio) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))

        return self.matricula


    def formataDataInicio(self):
        
        semestreInicio = str(self.semestreInicio)
        semestreInicio = list(semestreInicio)
        pre = semestreInicio[:1]
        pos = semestreInicio[1:5]

        pre = pre[0]
        pos = pos[0] + pos[1] + pos[2] + pos[3]

        semestreInicio = pre + '/' + pos
       
        return semestreInicio

    def formataDataFim(self):
        
        semestreFim = str(self.semestreFim)
        semestreFim = list(semestreFim)
        pre = semestreFim[:1]
        pos = semestreFim[1:5]

        pre = pre[0]
        pos = pos[0] + pos[1] + pos[2] + pos[3]

        semestreFim = pre + '/' + pos
       
        return semestreFim


