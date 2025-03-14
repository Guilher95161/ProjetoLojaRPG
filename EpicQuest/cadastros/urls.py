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
    
    path('listar/avaliacao/', AvaliacaoList.as_view(), name='listar-avaliacao'),
    path('cadastrar/avaliacao', AvaliacaoCreate.as_view(), name='cadastrar-avaliacao'),
    path('avaliacao/editar/<int:pk>/', AvaliacaoUpdate.as_view(), name='editar-avaliacao'),
    path('avaliacao/excluir/<int:pk>/', AvaliacaoDelete.as_view(), name='excluir-avaliacao'),

    path('listar/compra/',CompraList.as_view(), name='listar-compra'),

    path('listar/compra/<int:compra_id>/', ItemCompraList.as_view(), name='detalhar-compra'),

    path('cadastrar/plataforma/',PlataformaCreate.as_view(),name='cadastrar-plataforma'),
    path('editar/plataforma/<int:pk>/',PlataformaUpdate.as_view(),name='editar-plataforma' ),
    path('excluir/plataforma/<int:pk>',PlataformaDelete.as_view(),name='excluir-plataforma'),
    path('listar/plataforma/',PlataformaList.as_view(),name='listar-plataforma'),
]