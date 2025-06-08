"""
Módulo para registrar o histórico de movimentos no jogo de xadrez com explicações.
"""


class MovimentoXadrez:
    def __init__(self, peca, origem, destino, notacao, eh_captura=False, eh_xeque=False, eh_xeque_mate=False, promocao=None):
        self.peca = peca  # Nome da peça (ex: "Peão", "Torre", etc.)
        self.origem = origem  # Tupla (linha, coluna)
        self.destino = destino  # Tupla (linha, coluna)
        # Notação algébrica do movimento (ex: "e4", "Nf3", etc.)
        self.notacao = notacao
        self.eh_captura = eh_captura
        self.eh_xeque = eh_xeque
        self.eh_xeque_mate = eh_xeque_mate
        # Se for promoção de peão, indica a peça para qual foi promovido
        self.promocao = promocao
        self.explicacao = ""  # Explicação educativa sobre o movimento
        # Avaliação numérica do movimento (positiva favorece brancas, negativa favorece pretas)
        self.avaliacao = 0.0

    def adicionar_explicacao(self, explicacao):
        """Adiciona uma explicação educativa ao movimento"""
        self.explicacao = explicacao

    def adicionar_avaliacao(self, avaliacao):
        """Adiciona uma avaliação numérica ao movimento"""
        self.avaliacao = avaliacao

    def __str__(self):
        """Retorna uma representação em string do movimento"""
        resultado = self.notacao
        if self.eh_captura:
            resultado += " (captura)"
        if self.eh_xeque:
            resultado += " (xeque)"
        if self.eh_xeque_mate:
            resultado += " (xeque-mate)"
        if self.promocao:
            resultado += f" (promoção para {self.promocao})"
        return resultado


class HistoricoPartida:
    def __init__(self):
        self.movimentos = []
        self.indice_atual = -1  # Para navegação no histórico
        self.posicoes = []  # Lista de posições FEN para replay

    def adicionar_movimento(self, movimento, posicao_fen=None):
        """Adiciona um novo movimento ao histórico"""
        self.movimentos.append(movimento)
        if posicao_fen:
            self.posicoes.append(posicao_fen)
        self.indice_atual = len(self.movimentos) - 1

    def obter_movimento_atual(self):
        """Retorna o movimento atual baseado no índice"""
        if 0 <= self.indice_atual < len(self.movimentos):
            return self.movimentos[self.indice_atual]
        return None

    def obter_posicao_atual(self):
        """Retorna a posição FEN atual baseada no índice"""
        if 0 <= self.indice_atual < len(self.posicoes):
            return self.posicoes[self.indice_atual]
        return None

    def avancar(self):
        """Avança para o próximo movimento no histórico"""
        if self.indice_atual < len(self.movimentos) - 1:
            self.indice_atual += 1
            return True
        return False

    def retroceder(self):
        """Retrocede para o movimento anterior no histórico"""
        if self.indice_atual > 0:
            self.indice_atual -= 1
            return True
        return False

    def ir_para_inicio(self):
        """Vai para o início do histórico"""
        if len(self.movimentos) > 0:
            self.indice_atual = 0
            return True
        return False

    def ir_para_fim(self):
        """Vai para o fim do histórico"""
        if len(self.movimentos) > 0:
            self.indice_atual = len(self.movimentos) - 1
            return True
        return False

    def obter_notacao_partida(self):
        """Retorna a notação completa da partida"""
        resultado = []
        for i, movimento in enumerate(self.movimentos):
            if i % 2 == 0:  # Movimento das brancas
                resultado.append(f"{(i//2)+1}. {movimento.notacao}")
            else:  # Movimento das pretas
                resultado[-1] += f" {movimento.notacao}"
        return " ".join(resultado)

    def obter_explicacoes_partida(self):
        """Retorna todas as explicações da partida"""
        explicacoes = []
        for i, movimento in enumerate(self.movimentos):
            if movimento.explicacao:
                prefixo = f"{(i//2)+1}." if i % 2 == 0 else f"{(i//2)+1}..."
                explicacoes.append(
                    f"{prefixo} {movimento.notacao}: {movimento.explicacao}")
        return explicacoes

    def exportar_pgn(self, info_partida=None):
        """Exporta o histórico no formato PGN (Portable Game Notation)"""
        pgn = []

        # Adiciona as informações da partida
        if info_partida:
            for chave, valor in info_partida.items():
                pgn.append(f'[{chave} "{valor}"]')
            pgn.append("")  # Linha em branco após os cabeçalhos

        # Adiciona os movimentos
        texto_movimentos = []
        for i, movimento in enumerate(self.movimentos):
            if i % 2 == 0:  # Movimento das brancas
                texto_movimentos.append(f"{(i//2)+1}. {movimento.notacao}")
            else:  # Movimento das pretas
                texto_movimentos[-1] += f" {movimento.notacao}"

                # Adiciona comentários com explicações após cada par de movimentos
                if movimento.explicacao or self.movimentos[i-1].explicacao:
                    comentarios = []
                    if self.movimentos[i-1].explicacao:
                        comentarios.append(
                            f"Brancas: {self.movimentos[i-1].explicacao}")
                    if movimento.explicacao:
                        comentarios.append(f"Pretas: {movimento.explicacao}")
                    texto_movimentos[-1] += f" {{ {'; '.join(comentarios)} }}"

        pgn.append(" ".join(texto_movimentos))

        return "\n".join(pgn)


def converter_posicao_para_notacao(linha, coluna):
    """Converte uma posição (linha, coluna) para notação algébrica (ex: e4)"""
    colunas = "abcdefgh"
    linhas = "87654321"
    return colunas[coluna] + linhas[linha]


def criar_notacao_movimento(peca, origem, destino, eh_captura=False):
    """Cria a notação algébrica para um movimento"""
    peca_simbolos = {
        "Rei": "K",
        "Rainha": "Q",
        "Torre": "R",
        "Bispo": "B",
        "Cavalo": "N",
        "Peão": ""
    }

    simbolo_peca = peca_simbolos.get(peca, "")
    origem_notacao = converter_posicao_para_notacao(*origem)
    destino_notacao = converter_posicao_para_notacao(*destino)

    if peca == "Peão":
        if eh_captura:
            return origem_notacao[0] + "x" + destino_notacao
        else:
            return destino_notacao
    else:
        if eh_captura:
            return simbolo_peca + "x" + destino_notacao
        else:
            return simbolo_peca + destino_notacao
