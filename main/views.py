# Class Based Views
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


          
# # função utilizada para  devolver um valor em uma função de avaliação tardia,
# # que irá processar a url somente quando o dado for ser utilizado/visualizado. 
from django.urls import reverse_lazy

from main.models import Aluno



# View do cadastro do aluno
class AlunoDetailView(DetailView):

    model = Aluno
    template_name="main/cadastro_aluno.html"



# View da listagem dos alunos cadastrados
class PaginacaoListView(ListView):

    model = Aluno
    template_name="main/listagem_alunos.html"

    paginate_by = 10

    # Busca
    def get_queryset(self):

        busca_nome = self.request.GET.get('nome')

        if busca_nome:
            alunos = Aluno.objects.filter(nome__icontains=busca_nome)
        else: 
            alunos = Aluno.objects.all()
        

        return alunos



# View da criação de um novo cadastro de aluno
class AlunoCreateView(CreateView):
    model = Aluno
    fields = ['nome', 'curso', 'semestreInicio']
    template_name = 'main/novo_cadastro.html'
    success_url = ('/')


# View da atualização da ficha de um aluno já cadastrado
class AlunoUpdateView(UpdateView):
    model = Aluno
    fields = ['nome', 'curso', 'semestreInicio', 'semestreFim', 'situacao']
    template_name = 'main/atualizar_cadastro.html'
    template_name_suffix = '_update_form'
    success_url = ('/')


# View de deletar o cadastro do aluno
class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'main/deletar_cadastro.html'
    success_url = reverse_lazy('index')
