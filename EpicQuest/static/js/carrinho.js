document.addEventListener("DOMContentLoaded", function () {
    let carrinho = [];
  
    function adicionarAoCarrinho(jogoId, nome, preco) {
      let quantidadeInput = document.getElementById(`quantidade_${jogoId}`);
      let quantidade = parseInt(quantidadeInput.value);
  
      if (quantidade > 0) {
        let itemExistente = carrinho.find(item => item.jogoId === jogoId);
  
        if (itemExistente) {
          itemExistente.quantidade += quantidade;
        } else {
          carrinho.push({ jogoId, nome, preco, quantidade });
        }
  
        atualizarResumoCompra();
      }
    }
  
    function atualizarResumoCompra() {
      let resumoDiv = document.getElementById("resumo-compra");
      resumoDiv.innerHTML = "";
  
      if (carrinho.length === 0) {
        resumoDiv.innerHTML = "<p>Nenhum jogo adicionado ainda.</p>";
        return;
      }
  
      let lista = "<ul>";
      let total = 0;
  
      carrinho.forEach(item => {
        lista += `<li>${item.quantidade}x ${item.nome} - R$ ${(item.preco * item.quantidade).toFixed(2)}</li>`;
        total += item.preco * item.quantidade;
      });
  
      lista += `</ul><p><strong>Total: R$ ${total.toFixed(2)}</strong></p>`;
      resumoDiv.innerHTML = lista;
    }
  
    window.adicionarAoCarrinho = adicionarAoCarrinho;
  });