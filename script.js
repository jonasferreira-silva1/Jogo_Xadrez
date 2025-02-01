document.addEventListener("DOMContentLoaded", function () {
  const tabuleiroElement = document.getElementById("tabuleiro");

  // Estado inicial do tabuleiro com peças
  const estadoInicial = [
      ["torre-preta", "cavalo-preto", "bispo-preto", "rainha-preta", "rei-preto", "bispo-preto", "cavalo-preto", "torre-preto"],
      ["peao-preto", "peao-preto", "peao-preto", "peao-preto", "peao-preto", "peao-preto", "peao-preto", "peao-preto"],
      [null, null, null, null, null, null, null, null],
      [null, null, null, null, null, null, null, null],
      [null, null, null, null, null, null, null, null],
      [null, null, null, null, null, null, null, null],
      ["peao-branco", "peao-branco", "peao-branco", "peao-branco", "peao-branco", "peao-branco", "peao-branco", "peao-branco"],
      ["torre-branca", "cavalo-branco", "bispo-branco", "rainha-branca", "rei-branco", "bispo-branco", "cavalo-branco", "torre-branca"]
  ];

  // Cria o tabuleiro inicial
  for (let i = 0; i < 8; i++) {
      for (let j = 0; j < 8; j++) {
          const casa = document.createElement("div");
          casa.classList.add("casa");
          casa.classList.add((i + j) % 2 === 0 ? "branca" : "preta");
          casa.dataset.posicao = `${i}-${j}`;

          // Adiciona a peça à casa, se houver
          const peca = estadoInicial[i][j];
          if (peca) {
              const pecaElement = document.createElement("div");
              pecaElement.classList.add("peca");
              pecaElement.style.backgroundImage = `url('assets/${peca}.png')`; // Usa a imagem da peça
              casa.appendChild(pecaElement);
          }

          casa.addEventListener("click", selecionarPeca);
          tabuleiroElement.appendChild(casa);
      }
  }

  let turnoDoJogador = true; // Controla de quem é a vez
  let pecaSelecionada = null; // Armazena a peça selecionada pelo jogador

  function selecionarPeca(event) {
      const casaClicada = event.target.closest(".casa"); // Garante que o clique seja na casa
      if (!casaClicada) return; // Se não for uma casa, ignora

      const posicao = casaClicada.dataset.posicao;

      if (turnoDoJogador) {
          // Verifica se há uma peça na casa clicada
          const peca = casaClicada.querySelector(".peca");
          if (peca && peca.style.backgroundImage.includes("branco")) {
              // Seleciona a peça do jogador
              pecaSelecionada = { casa: casaClicada, posicao };
              console.log(`Jogador selecionou a peça na posição: ${posicao}`);
          } else if (pecaSelecionada) {
              // Tenta mover a peça selecionada para a nova posição
              moverPeca(pecaSelecionada.casa, casaClicada);
              pecaSelecionada = null;
              turnoDoJogador = false;
              movimentoDaMaquina();
          }
      }
  }

  function moverPeca(casaOrigem, casaDestino) {
      const peca = casaOrigem.querySelector(".peca");
      casaDestino.appendChild(peca);
  }

  function movimentoDaMaquina() {
      setTimeout(() => {
          const casas = document.querySelectorAll(".casa");
          const casasValidas = Array.from(casas).filter((casa) => {
              const peca = casa.querySelector(".peca");
              return peca && peca.style.backgroundImage.includes("preto"); // Seleciona peças pretas
          });

          if (casasValidas.length > 0) {
              const casaAleatoria = casasValidas[Math.floor(Math.random() * casasValidas.length)];
              const movimentosPossiveis = Array.from(casas).filter((casa) => !casa.querySelector(".peca"));

              if (movimentosPossiveis.length > 0) {
                  const movimentoAleatorio = movimentosPossiveis[Math.floor(Math.random() * movimentosPossiveis.length)];
                  moverPeca(casaAleatoria, movimentoAleatorio);
                  console.log(`Máquina moveu a peça para: ${movimentoAleatorio.dataset.posicao}`);
              }
          }

          turnoDoJogador = true;
      }, 1000); // Espera 1 segundo para simular o pensamento da máquina
  }
});
