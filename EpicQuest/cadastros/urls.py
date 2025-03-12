from django.urls import path
from .views import *
urlpatterns = [
    path('cadastrar/jogo/',JogoCreate.as_view(),name='cadastrar-jogo'),
    path('editar/jogo/<int:pk>/',JogoUpdate.as_view(),name='editar-jogo' ),
    path('excluir/jogo/<int:pk>',JogoDelete.as_view(),name='excluir-jogo'),
    path('listar/jogo/',JogoList.as_view(),name='listar-jogo'),
    path('finalizar-compra/', finalizar_compra, name='finalizar-compra'),
    path('cadastrar/categoria/',CategoriaCreate.as_view(),name='cadastrar-categoria'),
    path('editar/categoria/<int:pk>/',CategoriaUpdate.as_view(),name='editar-categoria' ),
    path('excluir/categoria/<int:pk>',CategoriaDelete.as_view(),name='excluir-categoria'),
    path('listar/categoria/',CategoriaList.as_view(),name='listar-categoria'),
]