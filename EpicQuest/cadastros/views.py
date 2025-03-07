from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .views import *
from .models import Jogo
from django.urls import reverse_lazy
# Create your views here.
class JogoCreate(CreateView):
    model = Jogo
    fields = ['nome','descricao','preco','estoque','lancamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')
class JogoUpdate(UpdateView):
    model = Jogo
    fields = ['nome','descricao','preco','estoque','lancamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')
class JogoDelete(DeleteView):
    model = Jogo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')
class JogoList(ListView):
    model = Jogo
    template_name = 'cadastros/listas/jogo.html'