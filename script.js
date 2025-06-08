document.addEventListener("DOMContentLoaded", function () {
  const tabuleiroElement = document.getElementById("tabuleiro");

  // Estado inicial do tabuleiro com peças
  const estadoInicial = [
    [
      "torre-preta",
      "cavalo-preto",
      "bispo-preto",
      "rainha-preta",
      "rei-preto",
      "bispo-preto",
      "cavalo-preto",
      "torre-preta",
    ],
    [
      "peao-preto",
      "peao-preto",
      "peao-preto",
      "peao-preto",
      "peao-preto",
      "peao-preto",
      "peao-preto",
      "peao-preto",
    ],
    [null, null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null, null],
    [
      "peao-branco",
      "peao-branco",
      "peao-branco",
      "peao-branco",
      "peao-branco",
      "peao-branco",
      "peao-branco",
      "peao-branco",
    ],
    [
      "torre-branca",
      "cavalo-branco",
      "bispo-branco",
      "rainha-branca",
      "rei-branco",
      "bispo-branco",
      "cavalo-branco",
      "torre-branca",
    ],
  ];

  // Histórico de movimentos
  const historicoMovimentos = [];
  let numeroJogada = 1;

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

  // Cria o painel de dicas e botões
  const painelControle = document.createElement("div");
  painelControle.id = "painel-controle";
  document.body.insertBefore(painelControle, tabuleiroElement.nextSibling);

  // Adiciona o botão de dica
  const botaoDica = document.createElement("button");
  botaoDica.id = "botao-dica";
  botaoDica.textContent = "Pedir Dica";
  botaoDica.addEventListener("click", pedirDica);
  painelControle.appendChild(botaoDica);

  // Adiciona o seletor de nível
  const seletorNivel = document.createElement("select");
  seletorNivel.id = "nivel-dificuldade";
  const niveis = ["Iniciante", "Intermediário", "Avançado"];
  niveis.forEach((nivel) => {
    const opcao = document.createElement("option");
    opcao.value = nivel.toLowerCase();
    opcao.textContent = nivel;
    seletorNivel.appendChild(opcao);
  });
  painelControle.appendChild(seletorNivel);

  // Adiciona o seletor de tutoriais
  const seletorTutorial = document.createElement("select");
  seletorTutorial.id = "tutorial-abertura";
  seletorTutorial.innerHTML = `
    <option value="">Selecione um tutorial...</option>
    <option value="ruy_lopez">Abertura Ruy López</option>
    <option value="defesa_siciliana">Defesa Siciliana</option>
    <option value="gambito_dama">Gambito da Dama</option>
    <option value="defesa_francesa">Defesa Francesa</option>
    <option value="abertura_inglesa">Abertura Inglesa</option>
  `;
  seletorTutorial.addEventListener("change", iniciarTutorial);
  painelControle.appendChild(seletorTutorial);

  // Cria o painel de mensagens
  const painelMensagens = document.createElement("div");
  painelMensagens.id = "painel-mensagens";
  document.body.insertBefore(painelMensagens, painelControle.nextSibling);

  // Cria o painel de histórico de movimentos
  const painelHistorico = document.createElement("div");
  painelHistorico.id = "painel-historico";
  painelHistorico.innerHTML = `
    <h3>Histórico de Movimentos</h3>
    <div id="lista-movimentos"></div>
    <div id="controles-historico">
      <button id="btn-inicio">⏮</button>
      <button id="btn-anterior">◀</button>
      <button id="btn-proximo">▶</button>
      <button id="btn-fim">⏭</button>
    </div>
  `;
  document.body.insertBefore(painelHistorico, painelMensagens.nextSibling);

  // Adiciona eventos aos botões de navegação do histórico
  document.getElementById("btn-inicio").addEventListener("click", irParaInicio);
  document
    .getElementById("btn-anterior")
    .addEventListener("click", movimentoAnterior);
  document
    .getElementById("btn-proximo")
    .addEventListener("click", proximoMovimento);
  document.getElementById("btn-fim").addEventListener("click", irParaFim);

  let turnoDoJogador = true; // Controla de quem é a vez
  let pecaSelecionada = null; // Armazena a peça selecionada pelo jogador
  let estadoAtualTabuleiro = [...estadoInicial]; // Copia o estado inicial
  let modoTutorial = false;
  let tutorialAtual = null;
  let passoTutorial = 0;

  function selecionarPeca(event) {
    const casaClicada = event.target.closest(".casa"); // Garante que o clique seja na casa
    if (!casaClicada) return; // Se não for uma casa, ignora

    const posicao = casaClicada.dataset.posicao;

    if (turnoDoJogador) {
      // Verifica se há uma peça na casa clicada
      const peca = casaClicada.querySelector(".peca");
      if (peca && peca.style.backgroundImage.includes("branco")) {
        // Remove destaque anterior, se houver
        document.querySelectorAll(".casa-destacada").forEach((casa) => {
          casa.classList.remove("casa-destacada");
        });

        // Seleciona a peça do jogador
        pecaSelecionada = { casa: casaClicada, posicao };
        casaClicada.classList.add("casa-destacada");
        console.log(`Jogador selecionou a peça na posição: ${posicao}`);

        // Mostra movimentos possíveis (simplificado)
        mostrarMovimentosPossiveis(posicao);
      } else if (pecaSelecionada) {
        // Tenta mover a peça selecionada para a nova posição
        const movimentoValido = moverPeca(pecaSelecionada.casa, casaClicada);

        if (movimentoValido) {
          // Remove todos os destaques
          document
            .querySelectorAll(".casa-destacada, .movimento-possivel")
            .forEach((casa) => {
              casa.classList.remove("casa-destacada");
              casa.classList.remove("movimento-possivel");
            });

          // Registra o movimento no histórico
          const [linhaOrigem, colunaOrigem] = pecaSelecionada.posicao
            .split("-")
            .map(Number);
          const [linhaDestino, colunaDestino] = posicao.split("-").map(Number);
          const nomePeca = obterNomePeca(
            pecaSelecionada.casa.querySelector(".peca").style.backgroundImage
          );
          const ehCaptura = casaClicada.querySelector(".peca") !== null;

          registrarMovimento(
            nomePeca,
            [linhaOrigem, colunaOrigem],
            [linhaDestino, colunaDestino],
            ehCaptura
          );

          pecaSelecionada = null;
          turnoDoJogador = false;

          // Atualiza o estado do tabuleiro
          atualizarEstadoTabuleiro();

          // Analisa o movimento do jogador e dá feedback
          analisarMovimentoJogador();

          setTimeout(() => {
            if (!modoTutorial) {
              movimentoDaMaquina();
            } else {
              avancarTutorial();
            }
          }, 1000);
        }
      }
    }
  }

  function obterNomePeca(backgroundImage) {
    // Extrai o nome da peça a partir da URL da imagem
    const match = backgroundImage.match(/\/([^/]+)\.png/);
    if (match) {
      const nomePeca = match[1];
      if (nomePeca.includes("peao")) return "Peão";
      if (nomePeca.includes("torre")) return "Torre";
      if (nomePeca.includes("cavalo")) return "Cavalo";
      if (nomePeca.includes("bispo")) return "Bispo";
      if (nomePeca.includes("rainha")) return "Rainha";
      if (nomePeca.includes("rei")) return "Rei";
    }
    return "Peça desconhecida";
  }

  function registrarMovimento(peca, origem, destino, ehCaptura) {
    // Converte posições para notação algébrica
    const colunas = "abcdefgh";
    const linhas = "87654321";
    const origemNotacao = colunas[origem[1]] + linhas[origem[0]];
    const destinoNotacao = colunas[destino[1]] + linhas[destino[0]];

    // Cria a notação do movimento
    let notacao = "";
    const pecaSimbolos = {
      Peão: "",
      Torre: "R",
      Cavalo: "N",
      Bispo: "B",
      Rainha: "Q",
      Rei: "K",
    };

    if (peca === "Peão") {
      if (ehCaptura) {
        notacao = origemNotacao[0] + "x" + destinoNotacao;
      } else {
        notacao = destinoNotacao;
      }
    } else {
      if (ehCaptura) {
        notacao = pecaSimbolos[peca] + "x" + destinoNotacao;
      } else {
        notacao = pecaSimbolos[peca] + destinoNotacao;
      }
    }

    // Cria objeto de movimento
    const movimento = {
      numero: Math.ceil(historicoMovimentos.length / 2) + 1,
      cor: historicoMovimentos.length % 2 === 0 ? "brancas" : "pretas",
      peca: peca,
      origem: origem,
      destino: destino,
      notacao: notacao,
      ehCaptura: ehCaptura,
      explicacao: "",
    };

    // Adiciona ao histórico
    historicoMovimentos.push(movimento);

    // Atualiza a exibição do histórico
    atualizarHistoricoVisual();
  }

  function atualizarHistoricoVisual() {
    const listaMovimentos = document.getElementById("lista-movimentos");
    listaMovimentos.innerHTML = "";

    let html = "";
    for (let i = 0; i < historicoMovimentos.length; i += 2) {
      const movBrancas = historicoMovimentos[i];
      const movPretas =
        i + 1 < historicoMovimentos.length ? historicoMovimentos[i + 1] : null;

      html += `<div class="jogada">
        <span class="numero">${Math.ceil((i + 1) / 2)}.</span>
        <span class="movimento brancas" data-indice="${i}">${
        movBrancas.notacao
      }</span>
        ${
          movPretas
            ? `<span class="movimento pretas" data-indice="${i + 1}">${
                movPretas.notacao
              }</span>`
            : ""
        }
      </div>`;
    }

    listaMovimentos.innerHTML = html;

    // Adiciona eventos de clique para mostrar explicações
    document.querySelectorAll(".movimento").forEach((elem) => {
      elem.addEventListener("click", function () {
        const indice = parseInt(this.dataset.indice);
        const movimento = historicoMovimentos[indice];
        if (movimento.explicacao) {
          exibirMensagem(movimento.explicacao);
        }
      });
    });
  }

  function irParaInicio() {
    // Implementação para voltar ao início da partida
    console.log("Voltando ao início da partida");
    // Aqui você restauraria o estado inicial do tabuleiro
  }

  function movimentoAnterior() {
    // Implementação para voltar um movimento
    console.log("Voltando um movimento");
    // Aqui você desfaria o último movimento
  }

  function proximoMovimento() {
    // Implementação para avançar um movimento
    console.log("Avançando um movimento");
    // Aqui você refaria o próximo movimento
  }

  function irParaFim() {
    // Implementação para ir até o final da partida
    console.log("Indo para o final da partida");
    // Aqui você avançaria até o estado atual do tabuleiro
  }

  function mostrarMovimentosPossiveis(posicao) {
    // Esta é uma versão simplificada. Em uma implementação real,
    // você calcularia os movimentos válidos com base nas regras do xadrez
    const [linha, coluna] = posicao.split("-").map(Number);

    // Exemplo: para um peão, mostra as casas à frente
    if (linha > 0) {
      const casaFrente = document.querySelector(
        `[data-posicao="${linha - 1}-${coluna}"]`
      );
      if (casaFrente && !casaFrente.querySelector(".peca")) {
        casaFrente.classList.add("movimento-possivel");
      }
    }

    // Implementação completa exigiria verificar todas as regras de movimento para cada tipo de peça
  }

  function moverPeca(casaOrigem, casaDestino) {
    const peca = casaOrigem.querySelector(".peca");

    // Verifica se o movimento é para uma casa destacada como possível
    if (
      !casaDestino.classList.contains("movimento-possivel") &&
      document.querySelectorAll(".movimento-possivel").length > 0
    ) {
      return false;
    }

    // Se houver uma peça na casa de destino, "captura" (remove)
    const pecaCapturada = casaDestino.querySelector(".peca");
    if (pecaCapturada) {
      casaDestino.removeChild(pecaCapturada);
    }

    casaDestino.appendChild(peca);
    return true;
  }

  function atualizarEstadoTabuleiro() {
    // Atualiza o estado interno do tabuleiro com base no DOM
    estadoAtualTabuleiro = Array(8)
      .fill()
      .map(() => Array(8).fill(null));

    document.querySelectorAll(".casa").forEach((casa) => {
      const [linha, coluna] = casa.dataset.posicao.split("-").map(Number);
      const peca = casa.querySelector(".peca");

      if (peca) {
        // Extrai o nome da peça do estilo de fundo
        const estiloBg = peca.style.backgroundImage;
        const nomePeca = estiloBg.substring(
          estiloBg.lastIndexOf("/") + 1,
          estiloBg.lastIndexOf(".")
        );
        estadoAtualTabuleiro[linha][coluna] = nomePeca;
      }
    });
  }

  function analisarMovimentoJogador() {
    // Em uma implementação real, você enviaria o estado do tabuleiro para o servidor
    // e receberia uma análise. Aqui, usamos mensagens genéricas para demonstração.
    const mensagens = [
      "Bom movimento! Você está desenvolvendo suas peças.",
      "Lembre-se de controlar o centro do tabuleiro.",
      "Cuidado com suas peças desprotegidas.",
      "Tente pensar alguns lances à frente.",
    ];

    const mensagemAleatoria =
      mensagens[Math.floor(Math.random() * mensagens.length)];

    // Adiciona a explicação ao último movimento no histórico
    if (historicoMovimentos.length > 0) {
      historicoMovimentos[historicoMovimentos.length - 1].explicacao =
        mensagemAleatoria;
      atualizarHistoricoVisual();
    }

    exibirMensagem(mensagemAleatoria);
  }

  function exibirMensagem(mensagem) {
    const painelMensagens = document.getElementById("painel-mensagens");
    painelMensagens.textContent = mensagem;
    painelMensagens.classList.add("mensagem-ativa");

    setTimeout(() => {
      painelMensagens.classList.remove("mensagem-ativa");
    }, 5000);
  }

  function pedirDica() {
    // Em uma implementação real, você enviaria o estado do tabuleiro para o servidor
    // Aqui, simulamos uma resposta
    const nivel = document.getElementById("nivel-dificuldade").value;

    exibirMensagem("Analisando posição...");

    setTimeout(() => {
      // Simula uma chamada ao servidor
      const dicas = {
        iniciante:
          "Tente mover um peão para o centro do tabuleiro para controlar mais espaço.",
        intermediário:
          "Considere desenvolver seus cavalos e bispos antes de mover muitos peões.",
        avançado:
          "Analise as fraquezas na estrutura de peões do adversário e planeje um ataque.",
      };

      exibirMensagem(dicas[nivel]);

      // Destaca uma jogada sugerida (simplificado)
      const casas = document.querySelectorAll(".casa");
      const casaAleatoria = casas[Math.floor(Math.random() * casas.length)];
      casaAleatoria.classList.add("jogada-sugerida");

      setTimeout(() => {
        casaAleatoria.classList.remove("jogada-sugerida");
      }, 3000);
    }, 1000);
  }

  function iniciarTutorial(event) {
    const tutorialSelecionado = event.target.value;
    if (!tutorialSelecionado) return;

    // Em uma implementação real, você carregaria os dados do tutorial do servidor
    // Aqui, usamos dados simulados
    const tutoriais = {
      ruy_lopez: {
        nome: "Abertura Ruy López",
        movimentos: [
          {
            origem: [6, 4],
            destino: [4, 4],
            explicacao:
              "Peão para e4: Controla o centro e abre caminho para o bispo e a rainha.",
          },
          {
            origem: [1, 4],
            destino: [3, 4],
            explicacao:
              "Peão para e5: Resposta simétrica, também controlando o centro.",
          },
          {
            origem: [7, 6],
            destino: [5, 5],
            explicacao:
              "Cavalo para f3: Desenvolve uma peça e ataca o peão em e5.",
          },
          {
            origem: [0, 1],
            destino: [2, 2],
            explicacao:
              "Cavalo para c6: Defende o peão em e5 e desenvolve uma peça.",
          },
          {
            origem: [7, 5],
            destino: [4, 2],
            explicacao:
              "Bispo para b5: O movimento característico da Ruy López, atacando o cavalo que defende o peão central.",
          },
        ],
      },
      // Adicione outros tutoriais aqui...
    };

    tutorialAtual = tutoriais[tutorialSelecionado];
    if (tutorialAtual) {
      modoTutorial = true;
      passoTutorial = 0;

      // Reseta o tabuleiro para o estado inicial
      resetarTabuleiro();

      // Inicia o tutorial
      exibirMensagem(`Tutorial iniciado: ${tutorialAtual.nome}`);
      avancarTutorial();
    }
  }

  function resetarTabuleiro() {
    // Remove todas as peças
    document.querySelectorAll(".peca").forEach((peca) => peca.remove());

    // Adiciona as peças na posição inicial
    for (let i = 0; i < 8; i++) {
      for (let j = 0; j < 8; j++) {
        const casa = document.querySelector(`[data-posicao="${i}-${j}"]`);
        const peca = estadoInicial[i][j];

        if (peca) {
          const pecaElement = document.createElement("div");
          pecaElement.classList.add("peca");
          pecaElement.style.backgroundImage = `url('assets/${peca}.png')`;
          casa.appendChild(pecaElement);
        }
      }
    }

    // Reseta o histórico
    historicoMovimentos.length = 0;
    atualizarHistoricoVisual();

    // Reseta o turno
    turnoDoJogador = true;
  }

  function avancarTutorial() {
    if (!tutorialAtual || passoTutorial >= tutorialAtual.movimentos.length) {
      modoTutorial = false;
      exibirMensagem("Tutorial concluído!");
      return;
    }

    const movimento = tutorialAtual.movimentos[passoTutorial];
    const casaOrigem = document.querySelector(
      `[data-posicao="${movimento.origem[0]}-${movimento.origem[1]}"]`
    );
    const casaDestino = document.querySelector(
      `[data-posicao="${movimento.destino[0]}-${movimento.destino[1]}"]`
    );

    // Destaca a peça a ser movida
    casaOrigem.classList.add("casa-destacada");

    setTimeout(() => {
      // Move a peça
      const peca = casaOrigem.querySelector(".peca");
      if (peca) {
        const ehCaptura = casaDestino.querySelector(".peca") !== null;
        if (ehCaptura) {
          casaDestino.querySelector(".peca").remove();
        }

        casaDestino.appendChild(peca);
        casaOrigem.classList.remove("casa-destacada");

        // Registra o movimento no histórico
        const nomePeca = obterNomePeca(peca.style.backgroundImage);
        registrarMovimento(
          nomePeca,
          movimento.origem,
          movimento.destino,
          ehCaptura
        );

        // Adiciona a explicação ao movimento
        if (historicoMovimentos.length > 0) {
          historicoMovimentos[historicoMovimentos.length - 1].explicacao =
            movimento.explicacao;
          atualizarHistoricoVisual();
        }

        // Exibe a explicação
        exibirMensagem(movimento.explicacao);

        // Avança para o próximo passo
        passoTutorial++;

        // Alterna o turno
        turnoDoJogador = !turnoDoJogador;

        // Continua o tutorial após um tempo
        setTimeout(() => {
          avancarTutorial();
        }, 3000);
      }
    }, 1000);
  }

  function movimentoDaMaquina() {
    setTimeout(() => {
      const casas = document.querySelectorAll(".casa");
      const casasValidas = Array.from(casas).filter((casa) => {
        const peca = casa.querySelector(".peca");
        return peca && peca.style.backgroundImage.includes("preto"); // Seleciona peças pretas
      });

      if (casasValidas.length > 0) {
        const casaAleatoria =
          casasValidas[Math.floor(Math.random() * casasValidas.length)];
        const movimentosPossiveis = Array.from(casas).filter(
          (casa) => !casa.querySelector(".peca")
        );

        if (movimentosPossiveis.length > 0) {
          const movimentoAleatorio =
            movimentosPossiveis[
              Math.floor(Math.random() * movimentosPossiveis.length)
            ];

          // Obtém as posições de origem e destino
          const [linhaOrigem, colunaOrigem] = casaAleatoria.dataset.posicao
            .split("-")
            .map(Number);
          const [linhaDestino, colunaDestino] =
            movimentoAleatorio.dataset.posicao.split("-").map(Number);

          // Move a peça
          const peca = casaAleatoria.querySelector(".peca");
          movimentoAleatorio.appendChild(peca);

          // Registra o movimento no histórico
          const nomePeca = obterNomePeca(peca.style.backgroundImage);
          registrarMovimento(
            nomePeca,
            [linhaOrigem, colunaOrigem],
            [linhaDestino, colunaDestino],
            false
          );

          console.log(
            `Máquina moveu a peça para: ${movimentoAleatorio.dataset.posicao}`
          );

          // Atualiza o estado do tabuleiro
          atualizarEstadoTabuleiro();

          // Explica o movimento da máquina (educativo)
          explicarMovimentoMaquina();
        }
      }

      turnoDoJogador = true;
    }, 1000); // Espera 1 segundo para simular o pensamento da máquina
  }

  function explicarMovimentoMaquina() {
    const nivel = document.getElementById("nivel-dificuldade").value;
    const explicacoes = {
      iniciante: [
        "Eu movi esta peça para desenvolver meu jogo.",
        "Este movimento me ajuda a controlar o centro.",
        "Estou protegendo minhas peças importantes.",
      ],
      intermediário: [
        "Este movimento prepara um ataque no flanco do rei.",
        "Estou melhorando a posição das minhas peças para o meio-jogo.",
        "Observe como estou tentando criar fraquezas na sua estrutura de peões.",
      ],
      avançado: [
        "Este movimento cria uma ameaça tática que você precisa responder.",
        "Estou implementando um plano estratégico de longo prazo.",
        "Observe como este movimento restringe a mobilidade das suas peças.",
      ],
    };

    const explicacoesNivel = explicacoes[nivel];
    const explicacao =
      explicacoesNivel[Math.floor(Math.random() * explicacoesNivel.length)];

    // Adiciona a explicação ao último movimento no histórico
    if (historicoMovimentos.length > 0) {
      historicoMovimentos[historicoMovimentos.length - 1].explicacao =
        explicacao;
      atualizarHistoricoVisual();
    }

    exibirMensagem(explicacao);
  }
});
