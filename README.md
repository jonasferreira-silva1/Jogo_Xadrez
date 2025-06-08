# Xadrez Educativo em desenvolvimento 

![Xadrez Educativo](assets/rei-branco.svg.png)

Um jogo de xadrez interativo com foco educacional, projetado para ensinar os fundamentos e estratégias do xadrez enquanto o usuário joga.

## 📋 Visão Geral

Este projeto combina uma interface web interativa com um backend Python poderoso para criar uma experiência de aprendizado completa de xadrez. O sistema não apenas permite jogar xadrez, mas também:

- Ensina as regras e movimentos básicos
- Fornece tutoriais interativos de aberturas clássicas
- Oferece lições progressivas por nível de habilidade
- Analisa movimentos e sugere melhorias
- Registra o histórico de jogadas com explicações educativas

## 🚀 Funcionalidades

- **Interface de Tabuleiro Interativa**: Tabuleiro de xadrez visual com seleção e movimentação de peças
- **Validação de Movimentos**: Implementação completa das regras do xadrez
- **Sistema de Dicas**: Botão de dica que sugere o próximo movimento com explicação
- **Tutoriais de Aberturas**: Aprenda aberturas clássicas como Ruy López, Defesa Siciliana, etc.
- **Lições Progressivas**: Conteúdo educativo organizado por níveis (iniciante, intermediário, avançado)
- **Análise de Movimentos**: Feedback educativo após cada movimento
- **Histórico de Partidas**: Registro de movimentos em notação algébrica com explicações
- **Integração com IA**: Usa o motor Stockfish para análises precisas (com modo fallback quando não disponível)

## 🛠️ Tecnologias Utilizadas

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python
- **Motor de Xadrez**: Stockfish (via biblioteca python-chess)
- **Servidor Web**: Flask

## 📁 Estrutura do Projeto

```
Jogo_Xadrez/
├── assets/              # Imagens das peças de xadrez
├── stockfish/           # Pasta para o motor Stockfish (opcional)
├── pecas.py             # Classes das peças com regras de movimento
├── xadrez.py            # Lógica principal do jogo
├── robo.py              # Integração com o motor Stockfish
├── tutoriais.py         # Tutoriais de aberturas clássicas
├── licoes.py            # Sistema de lições progressivas
├── historico.py         # Registro e análise de movimentos
├── server.py            # Servidor Flask para comunicação frontend/backend
├── index.html           # Página web principal
├── script.js            # Lógica da interface do usuário
├── styles.css           # Estilos da interface
└── README.md            # Este arquivo
```

## 📦 Componentes Principais

### Backend (Python)

#### pecas.py

Define as classes para todas as peças de xadrez com suas regras de movimento específicas:

- `Peca`: Classe base com métodos comuns
- Classes específicas: `Rei`, `Rainha`, `Torre`, `Bispo`, `Cavalo`, `Peao`
- Implementação de movimentos especiais (roque, en passant)

#### robo.py

Integração com o motor de xadrez Stockfish:

- `obter_melhor_jogada()`: Calcula a melhor jogada para uma posição
- `obter_dica_educativa()`: Fornece dicas contextuais baseadas na análise da posição
- Sistema de detecção automática do Stockfish com modo fallback

#### tutoriais.py

Sistema de tutoriais para aberturas clássicas:

- `AberturaTutorial`: Classe que gerencia tutoriais passo a passo
- Catálogo de aberturas famosas com explicações detalhadas
- Funções para navegar pelos tutoriais

#### licoes.py

Sistema de lições progressivas:

- `Licao`: Classe para lições com conteúdo e exercícios
- `ModuloLicoes`: Gerencia todas as lições disponíveis
- Organização por níveis de dificuldade

#### historico.py

Registro e análise de movimentos:

- `MovimentoXadrez`: Representa um movimento com notação e explicação
- `HistoricoPartida`: Gerencia o histórico completo de uma partida
- Funções para exportar partidas em formato PGN

#### server.py

Servidor Flask que expõe endpoints para o frontend:

- `/melhor_jogada`: Retorna a melhor jogada para uma posição
- `/dica_educativa`: Fornece dicas educativas contextuais
- Serve arquivos estáticos do frontend

### Frontend (Web)

#### index.html

Estrutura básica da página web com o tabuleiro de xadrez.

#### script.js

Lógica da interface do usuário:

- Renderização do tabuleiro e peças
- Interação com o usuário (seleção e movimento de peças)
- Sistema de tutoriais interativos
- Histórico visual de movimentos
- Comunicação com o backend via API

#### styles.css

Estilos visuais para todos os componentes:

- Tabuleiro e peças
- Painéis de controle e mensagens
- Histórico de movimentos
- Tutoriais e lições

## 🔧 Como Executar

### Pré-requisitos

1. Python 3.7 ou superior
2. Navegador web moderno (Chrome, Firefox, Edge, etc.)
3. Motor Stockfish (opcional, o sistema funciona sem ele)

### Instalação

1. Clone o repositório ou baixe os arquivos para seu computador:

```bash
git clone https://github.com/seu-usuario/xadrez-educativo.git
cd xadrez-educativo
```

2. Instale as dependências Python necessárias:

```bash
pip install flask python-chess
```

3. O motor Stockfish é opcional. O sistema irá procurar automaticamente por ele em locais comuns ou você pode colocá-lo na pasta `stockfish/`.

### Execução

1. Inicie o servidor Flask:

```bash
python server.py
```

2. Acesse o jogo em seu navegador:

```
http://localhost:5000
```

## 🎮 Como Jogar

1. **Movimentação das peças**:

   - Clique na peça que deseja mover
   - As casas para onde a peça pode se mover serão destacadas
   - Clique na casa de destino para completar o movimento
   - Você joga com as peças brancas, o computador responde com as pretas

2. **Recursos educativos**:

   - **Pedir Dica**: Clique no botão "Pedir Dica" para receber sugestões
   - **Histórico de Movimentos**: Veja todos os movimentos no painel à direita
   - **Navegação pelo histórico**: Use os botões ⏮ ◀ ▶ ⏭ para navegar pelos movimentos

3. **Níveis de dificuldade**:

   - Selecione o nível desejado no menu suspenso (Iniciante, Intermediário, Avançado)
   - Cada nível oferece dicas e análises adequadas ao seu conhecimento

4. **Tutoriais**:

   - Clique na aba "Tutoriais" no menu superior
   - Selecione uma abertura clássica para aprender
   - Siga as instruções passo a passo

5. **Lições**:
   - Acesse a aba "Lições" para conteúdo educativo organizado por nível
   - Escolha uma lição específica para aprender conceitos como táticas básicas, estruturas de peões, etc.

## ⚠️ Solução de Problemas

### Imagens de peças não carregam

Se algumas imagens de peças não estiverem carregando, verifique:

1. Se os nomes dos arquivos no diretório `assets/` correspondem aos nomes referenciados em `script.js`:

   - Os arquivos devem seguir o padrão: `[peça]-[cor].png`
   - Exemplo: `torre-branca.png`, `torre-preta.png`, etc.

2. Correções comuns:
   - Renomeie `torre-preto.png` para `torre-preta.png`
   - Verifique se `rei-branco.png` existe (além do `rei-branco.svg.png`)

### Servidor não inicia

Se o servidor Flask não iniciar:

1. Verifique se as dependências estão instaladas:

   ```bash
   pip install flask python-chess
   ```

2. Verifique se a porta 5000 não está sendo usada por outro aplicativo

### Stockfish não é encontrado

O sistema funcionará mesmo sem o Stockfish, usando um modo alternativo. Para usar o Stockfish:

1. Baixe o Stockfish para seu sistema operacional em [stockfishchess.org](https://stockfishchess.org/download/)
2. Coloque o executável em uma das seguintes localizações:
   - Na pasta `stockfish/` do projeto
   - Em um dos caminhos padrão listados em `robo.py`

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

## 🔍 Sobre a Arquitetura

Este projeto utiliza uma arquitetura híbrida com:

- **Frontend em JavaScript**: Para interatividade em tempo real no navegador
- **Backend em Python**: Para lógica complexa do jogo e integração com Stockfish

A comunicação entre frontend e backend é feita via API REST usando Flask, permitindo que a interface web consulte o motor de xadrez para análises e dicas.
