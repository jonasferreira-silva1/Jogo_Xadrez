"""
Módulo de lições progressivas para ensinar xadrez.
Este módulo contém lições organizadas por nível de dificuldade e tópicos específicos.
"""


class Licao:
    def __init__(self, titulo, descricao, conteudo, exercicios, nivel):
        self.titulo = titulo
        self.descricao = descricao
        self.conteudo = conteudo  # Lista de strings com o conteúdo da lição
        self.exercicios = exercicios  # Lista de dicionários com exercícios práticos
        self.nivel = nivel  # Iniciante, Intermediário ou Avançado
        self.concluida = False

    def marcar_como_concluida(self):
        self.concluida = True

    def verificar_resposta(self, exercicio_id, resposta):
        """Verifica se a resposta do exercício está correta"""
        if 0 <= exercicio_id < len(self.exercicios):
            exercicio = self.exercicios[exercicio_id]
            return resposta == exercicio["resposta_correta"]
        return False


class ModuloLicoes:
    def __init__(self):
        self.licoes = self._inicializar_licoes()
        self.licoes_por_nivel = {
            "iniciante": [licao for licao in self.licoes if licao.nivel == "iniciante"],
            "intermediario": [licao for licao in self.licoes if licao.nivel == "intermediario"],
            "avancado": [licao for licao in self.licoes if licao.nivel == "avancado"]
        }

    def _inicializar_licoes(self):
        """Inicializa todas as lições disponíveis"""
        return [
            # Lições para iniciantes
            Licao(
                titulo="Movimentos Básicos das Peças",
                descricao="Aprenda como cada peça se move no tabuleiro de xadrez.",
                conteudo=[
                    "O Peão: Move-se uma casa para frente, mas captura na diagonal. No primeiro movimento, pode avançar duas casas.",
                    "A Torre: Move-se em linha reta horizontalmente ou verticalmente, quantas casas quiser.",
                    "O Cavalo: Move-se em forma de 'L' (duas casas em uma direção e uma casa perpendicular). É a única peça que pode pular sobre outras.",
                    "O Bispo: Move-se na diagonal, quantas casas quiser.",
                    "A Rainha: Combina os movimentos da torre e do bispo, podendo mover-se em qualquer direção, quantas casas quiser.",
                    "O Rei: Move-se uma casa em qualquer direção."
                ],
                exercicios=[
                    {
                        "pergunta": "Qual peça se move apenas na diagonal?",
                        "opcoes": ["Torre", "Bispo", "Cavalo", "Peão"],
                        "resposta_correta": "Bispo"
                    },
                    {
                        "pergunta": "Qual peça pode pular sobre outras?",
                        "opcoes": ["Rainha", "Rei", "Cavalo", "Torre"],
                        "resposta_correta": "Cavalo"
                    }
                ],
                nivel="iniciante"
            ),

            Licao(
                titulo="Xeque e Xeque-mate",
                descricao="Aprenda o que é xeque, como defender-se dele e como dar xeque-mate.",
                conteudo=[
                    "Xeque: Quando o rei está ameaçado por uma peça adversária. O jogador deve obrigatoriamente sair do xeque.",
                    "Há três formas de sair de um xeque: mover o rei, capturar a peça atacante, ou bloquear o ataque com outra peça.",
                    "Xeque-mate: Quando o rei está em xeque e não há forma de sair dele. Isso encerra o jogo com vitória para quem deu o xeque-mate.",
                    "Afogamento: Quando o rei não está em xeque, mas o jogador não tem movimentos legais. Isso resulta em empate."
                ],
                exercicios=[
                    {
                        "pergunta": "Quais são as formas de sair de um xeque?",
                        "opcoes": [
                            "Apenas movendo o rei",
                            "Movendo o rei, capturando a peça atacante ou bloqueando o ataque",
                            "Rendendo-se",
                            "Movendo qualquer peça"
                        ],
                        "resposta_correta": "Movendo o rei, capturando a peça atacante ou bloqueando o ataque"
                    }
                ],
                nivel="iniciante"
            ),

            # Lições intermediárias
            Licao(
                titulo="Táticas Básicas",
                descricao="Aprenda táticas fundamentais como garfos, espetos e cravadas.",
                conteudo=[
                    "Garfo: Uma peça ataca duas ou mais peças adversárias simultaneamente.",
                    "Espeto: Uma peça ataca duas peças adversárias em uma linha, sendo que a peça mais valiosa está atrás.",
                    "Cravada: Uma peça não pode se mover porque exporia uma peça mais valiosa atrás dela.",
                    "Essas táticas permitem ganhar material ou obter vantagem posicional."
                ],
                exercicios=[
                    {
                        "pergunta": "O que é um 'garfo' no xadrez?",
                        "opcoes": [
                            "Uma peça que não pode se mover",
                            "Uma peça que ataca duas ou mais peças simultaneamente",
                            "Um tipo de defesa",
                            "Um movimento especial do rei"
                        ],
                        "resposta_correta": "Uma peça que ataca duas ou mais peças simultaneamente"
                    }
                ],
                nivel="intermediario"
            ),

            Licao(
                titulo="Estruturas de Peões",
                descricao="Aprenda sobre diferentes estruturas de peões e sua importância estratégica.",
                conteudo=[
                    "A estrutura de peões define a característica da posição e influencia o plano de jogo.",
                    "Peões isolados: Peões sem peões aliados em colunas adjacentes. São geralmente uma fraqueza.",
                    "Peões dobrados: Dois peões da mesma cor na mesma coluna. Podem ser uma fraqueza, mas também podem controlar casas importantes.",
                    "Peões passados: Peões que não têm peões adversários à sua frente ou em colunas adjacentes. São potencialmente fortes no final de jogo."
                ],
                exercicios=[
                    {
                        "pergunta": "O que é um peão passado?",
                        "opcoes": [
                            "Um peão que foi capturado",
                            "Um peão que não pode se mover",
                            "Um peão sem peões adversários à sua frente ou em colunas adjacentes",
                            "Um peão na mesma coluna que outro peão aliado"
                        ],
                        "resposta_correta": "Um peão sem peões adversários à sua frente ou em colunas adjacentes"
                    }
                ],
                nivel="intermediario"
            ),

            # Lições avançadas
            Licao(
                titulo="Finais de Rei e Peão",
                descricao="Aprenda princípios fundamentais dos finais de rei e peão.",
                conteudo=[
                    "Regra do quadrado: Determina se um rei pode alcançar um peão adversário.",
                    "Oposição: Uma posição onde os reis estão frente a frente com uma casa entre eles. Quem tem que mover geralmente está em desvantagem.",
                    "Peões passados distantes: Dois peões passados distantes um do outro podem ser decisivos, pois o rei adversário não pode parar ambos.",
                    "Triangulação: Técnica para perder um tempo e forçar o adversário a mover seu rei para uma posição desfavorável."
                ],
                exercicios=[
                    {
                        "pergunta": "O que é a 'oposição' em finais de rei e peão?",
                        "opcoes": [
                            "Quando os reis estão em lados opostos do tabuleiro",
                            "Quando os reis estão frente a frente com uma casa entre eles",
                            "Quando um rei está em xeque",
                            "Quando um peão está prestes a promover"
                        ],
                        "resposta_correta": "Quando os reis estão frente a frente com uma casa entre eles"
                    }
                ],
                nivel="avancado"
            ),

            Licao(
                titulo="Sacrifícios Posicionais",
                descricao="Aprenda a avaliar e executar sacrifícios posicionais para obter vantagem a longo prazo.",
                conteudo=[
                    "Sacrifício posicional: Entrega voluntária de material para obter vantagem posicional ou iniciativa.",
                    "Diferente dos sacrifícios táticos, os sacrifícios posicionais nem sempre têm compensação imediata visível.",
                    "Fatores a considerar: atividade das peças, estrutura de peões, segurança do rei, controle de casas importantes.",
                    "Exemplos famosos incluem o 'Sacrifício de Peão Grunfeld' e o 'Sacrifício de Qualidade'."
                ],
                exercicios=[
                    {
                        "pergunta": "Qual a diferença entre um sacrifício tático e um sacrifício posicional?",
                        "opcoes": [
                            "Não há diferença",
                            "Sacrifícios táticos envolvem apenas peões",
                            "Sacrifícios posicionais têm compensação imediata, táticos são a longo prazo",
                            "Sacrifícios táticos têm compensação concreta e imediata, posicionais têm vantagens a longo prazo"
                        ],
                        "resposta_correta": "Sacrifícios táticos têm compensação concreta e imediata, posicionais têm vantagens a longo prazo"
                    }
                ],
                nivel="avancado"
            )
        ]

    def obter_licoes_por_nivel(self, nivel):
        """Retorna todas as lições de um determinado nível"""
        return self.licoes_por_nivel.get(nivel.lower(), [])

    def obter_proxima_licao_nao_concluida(self, nivel):
        """Retorna a próxima lição não concluída de um determinado nível"""
        licoes = self.obter_licoes_por_nivel(nivel)
        for licao in licoes:
            if not licao.concluida:
                return licao
        return None

    def obter_licao_por_titulo(self, titulo):
        """Retorna uma lição específica pelo título"""
        for licao in self.licoes:
            if licao.titulo.lower() == titulo.lower():
                return licao
        return None


# Instância global do módulo de lições
modulo_licoes = ModuloLicoes()
