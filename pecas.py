class Peca:
    def __init__(self, cor):
        self.cor = cor
        # Para controlar se a peça já foi movida (útil para roque e movimento inicial de peões)
        self.movida = False

    def movimentos_validos(self, posicao_atual, tabuleiro):
        pass

    def esta_no_tabuleiro(self, linha, coluna):
        return 0 <= linha < 8 and 0 <= coluna < 8

    def caminho_livre(self, posicao_atual, destino, tabuleiro):
        """Verifica se o caminho entre a posição atual e o destino está livre"""
        linha_atual, coluna_atual = posicao_atual
        linha_destino, coluna_destino = destino

        # Determina a direção do movimento
        delta_linha = 0 if linha_atual == linha_destino else (
            1 if linha_destino > linha_atual else -1)
        delta_coluna = 0 if coluna_atual == coluna_destino else (
            1 if coluna_destino > coluna_atual else -1)

        linha, coluna = linha_atual + delta_linha, coluna_atual + delta_coluna

        # Verifica cada casa no caminho (exceto a posição atual e o destino)
        while (linha, coluna) != (linha_destino, coluna_destino):
            if tabuleiro[linha][coluna] is not None:
                return False
            linha += delta_linha
            coluna += delta_coluna

        return True


class Rei(Peca):
    def movimentos_validos(self, posicao_atual, tabuleiro):
        linha, coluna = posicao_atual
        movimentos = []

        # Direções possíveis para o rei (horizontal, vertical e diagonal)
        direcoes = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for delta_linha, delta_coluna in direcoes:
            nova_linha, nova_coluna = linha + delta_linha, coluna + delta_coluna

            # Verifica se a nova posição está dentro do tabuleiro
            if self.esta_no_tabuleiro(nova_linha, nova_coluna):
                # Verifica se a casa está vazia ou tem uma peça adversária
                peca_destino = tabuleiro[nova_linha][nova_coluna]
                if peca_destino is None or peca_destino.cor != self.cor:
                    movimentos.append((nova_linha, nova_coluna))

        # Adicionar lógica para roque (se o rei não foi movido e as torres estão nas posições iniciais)
        if not self.movida:
            # Roque pequeno (lado do rei)
            if (coluna + 3 < 8 and
                tabuleiro[linha][coluna + 3] is not None and
                isinstance(tabuleiro[linha][coluna + 3], Torre) and
                not tabuleiro[linha][coluna + 3].movida and
                tabuleiro[linha][coluna + 1] is None and
                    tabuleiro[linha][coluna + 2] is None):
                movimentos.append((linha, coluna + 2))

            # Roque grande (lado da rainha)
            if (coluna - 4 >= 0 and
                tabuleiro[linha][coluna - 4] is not None and
                isinstance(tabuleiro[linha][coluna - 4], Torre) and
                not tabuleiro[linha][coluna - 4].movida and
                tabuleiro[linha][coluna - 1] is None and
                tabuleiro[linha][coluna - 2] is None and
                    tabuleiro[linha][coluna - 3] is None):
                movimentos.append((linha, coluna - 2))

        return movimentos


class Rainha(Peca):
    def movimentos_validos(self, posicao_atual, tabuleiro):
        linha, coluna = posicao_atual
        movimentos = []

        # Direções possíveis para a rainha (combinação de torre e bispo)
        direcoes = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for delta_linha, delta_coluna in direcoes:
            for distancia in range(1, 8):  # Máximo de 7 casas em qualquer direção
                nova_linha = linha + delta_linha * distancia
                nova_coluna = coluna + delta_coluna * distancia

                # Verifica se a nova posição está dentro do tabuleiro
                if not self.esta_no_tabuleiro(nova_linha, nova_coluna):
                    break

                # Verifica se a casa está vazia
                if tabuleiro[nova_linha][nova_coluna] is None:
                    movimentos.append((nova_linha, nova_coluna))
                else:
                    # Se houver uma peça adversária, pode capturar e para
                    if tabuleiro[nova_linha][nova_coluna].cor != self.cor:
                        movimentos.append((nova_linha, nova_coluna))
                    break  # Não pode pular sobre peças

        return movimentos


class Torre(Peca):
    def movimentos_validos(self, posicao_atual, tabuleiro):
        linha, coluna = posicao_atual
        movimentos = []

        # Direções possíveis para a torre (horizontal e vertical)
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for delta_linha, delta_coluna in direcoes:
            for distancia in range(1, 8):  # Máximo de 7 casas em qualquer direção
                nova_linha = linha + delta_linha * distancia
                nova_coluna = coluna + delta_coluna * distancia

                # Verifica se a nova posição está dentro do tabuleiro
                if not self.esta_no_tabuleiro(nova_linha, nova_coluna):
                    break

                # Verifica se a casa está vazia
                if tabuleiro[nova_linha][nova_coluna] is None:
                    movimentos.append((nova_linha, nova_coluna))
                else:
                    # Se houver uma peça adversária, pode capturar e para
                    if tabuleiro[nova_linha][nova_coluna].cor != self.cor:
                        movimentos.append((nova_linha, nova_coluna))
                    break  # Não pode pular sobre peças

        return movimentos


class Bispo(Peca):
    def movimentos_validos(self, posicao_atual, tabuleiro):
        linha, coluna = posicao_atual
        movimentos = []

        # Direções possíveis para o bispo (diagonais)
        direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for delta_linha, delta_coluna in direcoes:
            for distancia in range(1, 8):  # Máximo de 7 casas em qualquer direção
                nova_linha = linha + delta_linha * distancia
                nova_coluna = coluna + delta_coluna * distancia

                # Verifica se a nova posição está dentro do tabuleiro
                if not self.esta_no_tabuleiro(nova_linha, nova_coluna):
                    break

                # Verifica se a casa está vazia
                if tabuleiro[nova_linha][nova_coluna] is None:
                    movimentos.append((nova_linha, nova_coluna))
                else:
                    # Se houver uma peça adversária, pode capturar e para
                    if tabuleiro[nova_linha][nova_coluna].cor != self.cor:
                        movimentos.append((nova_linha, nova_coluna))
                    break  # Não pode pular sobre peças

        return movimentos


class Cavalo(Peca):
    def movimentos_validos(self, posicao_atual, tabuleiro):
        linha, coluna = posicao_atual
        movimentos = []

        # Movimentos em "L" do cavalo
        movimentos_l = [
            (linha - 2, coluna - 1), (linha - 2, coluna + 1),
            (linha - 1, coluna - 2), (linha - 1, coluna + 2),
            (linha + 1, coluna - 2), (linha + 1, coluna + 2),
            (linha + 2, coluna - 1), (linha + 2, coluna + 1)
        ]

        for nova_linha, nova_coluna in movimentos_l:
            # Verifica se a nova posição está dentro do tabuleiro
            if self.esta_no_tabuleiro(nova_linha, nova_coluna):
                # Verifica se a casa está vazia ou tem uma peça adversária
                peca_destino = tabuleiro[nova_linha][nova_coluna]
                if peca_destino is None or peca_destino.cor != self.cor:
                    movimentos.append((nova_linha, nova_coluna))

        return movimentos


class Peao(Peca):
    def movimentos_validos(self, posicao_atual, tabuleiro):
        linha, coluna = posicao_atual
        movimentos = []

        # Direção do movimento depende da cor
        direcao = -1 if self.cor == "branco" else 1

        # Movimento para frente (1 casa)
        nova_linha = linha + direcao
        if self.esta_no_tabuleiro(nova_linha, coluna) and tabuleiro[nova_linha][coluna] is None:
            movimentos.append((nova_linha, coluna))

            # Movimento inicial (2 casas)
            if ((self.cor == "branco" and linha == 6) or (self.cor == "preto" and linha == 1)) and not self.movida:
                nova_linha = linha + 2 * direcao
                if self.esta_no_tabuleiro(nova_linha, coluna) and tabuleiro[nova_linha][coluna] is None:
                    movimentos.append((nova_linha, coluna))

        # Capturas nas diagonais
        for delta_coluna in [-1, 1]:
            nova_linha = linha + direcao
            nova_coluna = coluna + delta_coluna

            if self.esta_no_tabuleiro(nova_linha, nova_coluna):
                peca_destino = tabuleiro[nova_linha][nova_coluna]
                if peca_destino is not None and peca_destino.cor != self.cor:
                    movimentos.append((nova_linha, nova_coluna))

                # En passant (implementação básica)
                # Para uma implementação completa, precisaríamos rastrear o último movimento do oponente

        return movimentos
