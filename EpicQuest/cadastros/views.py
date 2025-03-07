from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from braces.views import LoginRequiredMixin,GroupRequiredMixin
from .views import *
from .models import Jogo

# Create your views here.
class JogoCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    group_required = ["Administrador","Funcionario"]
    model = Jogo
    fields = ['nome','descricao','preco','estoque','lancamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-jogo')
    login_url = reverse_lazy('login')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo jogo"
        context['botao'] = "Cadastrar"
        return context

class JogoUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    group_required = ["Administrador","Funcionario"]
    model = Jogo
    fields = ['nome','descricao','preco','estoque','lancamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-jogo')
    login_url = reverse_lazy('login')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Atualização de jogo"
        context['botao'] = "Atualizar"
        return context
class JogoDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    group_required = ["Administrador","Funcionario"]
    model = Jogo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-jogo')
    login_url = reverse_lazy('login')
    
class JogoList(ListView):
    model = Jogo
    template_name = 'cadastros/listas/jogo.html'