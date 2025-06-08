"""
Módulo de tutoriais de aberturas clássicas para o jogo de xadrez.
Este módulo contém definições de aberturas famosas e tutoriais passo a passo.
"""


class AberturaTutorial:
    def __init__(self, nome, descricao, movimentos, dicas):
        self.nome = nome
        self.descricao = descricao
        # Lista de tuplas (origem, destino, explicação)
        self.movimentos = movimentos
        self.dicas = dicas  # Lista de dicas estratégicas para esta abertura
        self.passo_atual = 0

    def proximo_movimento(self):
        """Retorna o próximo movimento do tutorial e sua explicação"""
        if self.passo_atual < len(self.movimentos):
            movimento = self.movimentos[self.passo_atual]
            self.passo_atual += 1
            return movimento
        return None

    def reiniciar(self):
        """Reinicia o tutorial para o início"""
        self.passo_atual = 0

    def progresso(self):
        """Retorna o progresso atual do tutorial"""
        return self.passo_atual, len(self.movimentos)


# Catálogo de aberturas clássicas
ABERTURAS = {
    "ruy_lopez": AberturaTutorial(
        nome="Abertura Ruy López",
        descricao="Uma das aberturas mais antigas e respeitadas. Começa com 1.e4 e5 2.Nf3 Nc6 3.Bb5, atacando o cavalo que defende o peão em e5.",
        movimentos=[
            ((6, 4), (4, 4), "Peão para e4: Controla o centro e abre caminho para o bispo e a rainha."),
            ((1, 4), (3, 4), "Peão para e5: Resposta simétrica, também controlando o centro."),
            ((7, 6), (5, 5), "Cavalo para f3: Desenvolve uma peça e ataca o peão em e5."),
            ((0, 1), (2, 2), "Cavalo para c6: Defende o peão em e5 e desenvolve uma peça."),
            ((7, 5), (4, 2), "Bispo para b5: O movimento característico da Ruy López, atacando o cavalo que defende o peão central.")
        ],
        dicas=[
            "O objetivo principal da Ruy López é exercer pressão sobre o centro e, eventualmente, sobre o peão em e5.",
            "O bispo em b5 ameaça capturar o cavalo em c6, o que forçaria a recaptura com o peão e criaria uma estrutura de peões dobrados.",
            "Esta abertura geralmente leva a um jogo posicional complexo com muitas possibilidades estratégicas."
        ]
    ),

    "defesa_siciliana": AberturaTutorial(
        nome="Defesa Siciliana",
        descricao="Uma das defesas mais populares contra 1.e4, onde as pretas respondem com 1...c5, lutando assimetricamente pelo centro.",
        movimentos=[
            ((6, 4), (4, 4), "Peão para e4: Controla o centro e abre caminho para o bispo e a rainha."),
            ((1, 2), (3, 2), "Peão para c5: A característica da Defesa Siciliana, controlando d4 assimetricamente."),
            ((7, 6), (5, 5), "Cavalo para f3: Desenvolve uma peça e prepara-se para controlar o centro."),
            ((0, 1), (2, 2), "Cavalo para c6: Desenvolve uma peça e prepara-se para controlar o centro.")
        ],
        dicas=[
            "A Defesa Siciliana cria uma posição assimétrica desde o início, o que geralmente leva a um jogo dinâmico.",
            "As pretas lutam pelo controle da casa d4 com o peão em c5, em vez de jogar simetricamente com e5.",
            "Esta defesa é conhecida por suas muitas variantes e possibilidades táticas."
        ]
    ),

    "gambito_dama": AberturaTutorial(
        nome="Gambito da Dama",
        descricao="Uma abertura popular que começa com 1.d4 d5 2.c4, oferecendo um peão para ganhar desenvolvimento e controle do centro.",
        movimentos=[
            ((6, 3), (4, 3), "Peão para d4: Controla o centro com um peão."),
            ((1, 3), (3, 3), "Peão para d5: Resposta simétrica, também controlando o centro."),
            ((6, 2), (4, 2), "Peão para c4: O movimento característico do Gambito da Dama, oferecendo um peão para ganhar controle do centro.")
        ],
        dicas=[
            "O Gambito da Dama não é um verdadeiro gambito, pois é difícil para as pretas manter o peão extra.",
            "O objetivo das brancas é estabelecer um forte centro de peões e desenvolver suas peças harmoniosamente.",
            "Esta abertura geralmente leva a posições sólidas com muitas possibilidades estratégicas."
        ]
    ),

    "defesa_francesa": AberturaTutorial(
        nome="Defesa Francesa",
        descricao="Uma defesa sólida que começa com 1.e4 e6, preparando-se para contestar o centro com d5.",
        movimentos=[
            ((6, 4), (4, 4), "Peão para e4: Controla o centro e abre caminho para o bispo e a rainha."),
            ((1, 4), (2, 4), "Peão para e6: Prepara o avanço do peão para d5 sem bloquear o bispo de c8."),
            ((6, 3), (4, 3), "Peão para d4: Estabelece um forte centro de peões."),
            ((1, 3), (3, 3), "Peão para d5: Contesta o centro e cria uma estrutura de peões característica da Defesa Francesa.")
        ],
        dicas=[
            "A Defesa Francesa cria uma estrutura de peões sólida, mas pode limitar temporariamente o desenvolvimento do bispo de casas claras.",
            "As pretas geralmente buscam contra-atacar no flanco da dama, enquanto as brancas frequentemente atacam no flanco do rei.",
            "Esta defesa é conhecida por suas posições fechadas e jogo estratégico."
        ]
    ),

    "abertura_inglesa": AberturaTutorial(
        nome="Abertura Inglesa",
        descricao="Uma abertura flexível que começa com 1.c4, controlando o centro indiretamente.",
        movimentos=[
            ((6, 2), (4, 2), "Peão para c4: Controla o centro indiretamente e prepara um desenvolvimento flexível."),
            ((1, 4), (3, 4), "Peão para e5: Uma resposta comum, controlando o centro diretamente."),
            ((7, 1), (5, 2), "Cavalo para c3: Desenvolve uma peça e controla o centro.")
        ],
        dicas=[
            "A Abertura Inglesa é muito flexível e pode transpor para muitas outras aberturas.",
            "As brancas geralmente buscam controlar o centro indiretamente, em vez de ocupá-lo imediatamente com peões.",
            "Esta abertura é conhecida por suas possibilidades estratégicas e posicionais."
        ]
    )
}


def obter_tutorial(nome_abertura):
    """Retorna um tutorial específico pelo nome da abertura"""
    return ABERTURAS.get(nome_abertura)


def listar_tutoriais():
    """Retorna uma lista de todos os tutoriais disponíveis"""
    return [(nome, abertura.nome, abertura.descricao) for nome, abertura in ABERTURAS.items()]
