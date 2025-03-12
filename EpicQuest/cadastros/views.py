from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from braces.views import LoginRequiredMixin,GroupRequiredMixin
from django.db import transaction
from .views import *
from .models import ItemCompra, Jogo,Compra,Categoria

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

class CompraCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Cliente", u"Administrador"]
    model = Compra
    fields = []  # Não precisamos expor campos diretamente, pois os dados vêm do formulário via POST
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-compras')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        """ Define o usuário da compra e processa os itens """
        form.instance.usuario = self.request.user

        with transaction.atomic():  # Garante que toda a operação seja concluída corretamente
            compra = form.save()  # Salva a compra
            itens = self.request.POST.getlist('itens[]')  # Recebe os itens do formulário (deve ser uma lista JSON)

            preco_total = 0
            for item in itens:
                jogo_id = int(item.get("jogo_id"))
                quantidade = int(item.get("quantidade"))

                jogo = Jogo.objects.select_for_update().get(id=jogo_id)

                # Criando item da compra
                ItemCompra.objects.create(compra=compra, jogo=jogo, quantidade=quantidade)

                # Atualizando estoque
                jogo.estoque -= quantidade
                jogo.save()

                # Calculando preço total
                preco_total += jogo.preco * quantidade

            # Atualiza o preço total da compra
            compra.preco_total = preco_total
            compra.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Adiciona variáveis extras ao template """
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Finalizar Compra"
        context['botao'] = "Comprar"
        context['jogos'] = Jogo.objects.filter(estoque__gt=0)  # Só mostra jogos disponíveis
        return context

@login_required
def finalizar_compra(request):
    if request.method == "POST":
        usuario = request.user
        itens_comprados = []
        preco_total = 0

        for key, value in request.POST.items():
            if key.startswith("quantidade_"):
                jogo_id = key.split("_")[1]  # Extrai o ID do jogo
                quantidade = int(value)

                if quantidade > 0:
                    jogo = Jogo.objects.get(id=jogo_id)

                    if jogo.estoque >= quantidade:
                        preco_total += jogo.preco * quantidade
                        itens_comprados.append((jogo, quantidade))
                    else:
                        messages.error(request, f"Estoque insuficiente para {jogo.nome}.")
                        return redirect('listar-jogo')

        if not itens_comprados:
            messages.error(request, "Nenhum jogo foi selecionado.")
            return redirect('listar-jogo')

        # Criar a compra
        compra = Compra.objects.create(usuario=usuario, precoTotal=preco_total, dataCompra=now())

        # Criar os itens da compra e atualizar o estoque
        for jogo, quantidade in itens_comprados:
            ItemCompra.objects.create(compra=compra, jogo=jogo, quantidade=quantidade)
            jogo.estoque -= quantidade  # Atualiza o estoque
            jogo.save()

        messages.success(request, "Compra finalizada com sucesso!")
        return redirect('listar-jogo')

    return redirect('listar-jogo')

'''CompraList vai listar todas as compras existentes caso seja um administrador
Vai ter um botão e caso o administrador clique nesse botão, irá aparecer todos os itens comprados por aquele usuário'''
class CategoriaCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    group_required = ["Administrador","Funcionario"]
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')
    login_url = reverse_lazy('login')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de Novo Categoria"
        context['botao'] = "Cadastrar"
        return context

class CategoriaUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    group_required = ["Administrador","Funcionario"]
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')
    login_url = reverse_lazy('login')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Atualização de Categoria"
        context['botao'] = "Atualizar"
        return context
class CategoriaDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    group_required = ["Administrador","Funcionario"]
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')
    login_url = reverse_lazy('login')
    
class CategoriaList(ListView):
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'

#Avaliação só existirá para cada jogo e de cada usuário e o usuário já deve ter feito uma compra de jogo, só o usuario pode criar, mas o RUD, todos podem fazer, só para aquele usuário especifico aparecerá os seus e para o Funcionario e Administrador o de todo mundo