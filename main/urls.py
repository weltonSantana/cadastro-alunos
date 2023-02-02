from django.urls import path

from main.views import AlunoDetailView, PaginacaoListView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView

urlpatterns = [
    path('', PaginacaoListView.as_view(), name='index'),
    path('cadastroAluno/<int:pk>', AlunoDetailView.as_view()  , name='ficha-view'),
    path('novoCadastro/', AlunoCreateView.as_view(), name='novo-cad'),
    path('atualizarCadastro/<int:pk>', AlunoUpdateView.as_view()  , name='att-view'),
    path('deletarCadastro/<int:pk>', AlunoDeleteView.as_view(), name='deletar-cad' ),
]