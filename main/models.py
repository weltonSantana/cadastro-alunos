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

        semestreInicio = str(self.semestreInicio)
        semestreInicio = list(semestreInicio)

        semestreFim = str(self.semestreFim)
        semestreFim = list(semestreFim)

        pos1 = semestreInicio[1:5]
        pos2 = semestreFim[1:5]

        def convert(list):  
            s = [str(i) for i in list]  
            res = int("".join(s))   
            return(res) 

      
        if self.semestreInicio > 99999 or self.semestreInicio < 10000:
            raise ValidationError('Não é possivel!') 

        Inicio = int(convert(pos1))

        if self.semestreFim > 99999 or self.semestreFim < 10000:
            raise ValidationError('Não é possivel!') 
        else:
          if self.semestreFim != None:
             Fim = int(convert(pos2))
         
        if self.semestreFim == None:
            return self.semestreFim
        elif Fim <= Inicio:
            raise ValidationError('Não é possivel terminar o semestre antes do seu inicio!') 
        elif Fim > Inicio and self.situacao == 'Ativo':
            raise ValidationError('Não é possivel terminar o semestre e continuar ativo!') 
        elif Fim > Inicio and Fim < Inicio + 4 and self.situacao == 'Formado':
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


