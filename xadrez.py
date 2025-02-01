from pecas import Rei, Rainha, Torre, Bispo, Cavalo, Peao
from robo import obter_melhor_jogada
import chess


class Tabuleiro:
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro_inicial()

    def criar_tabuleiro_inicial(self):
        tabuleiro = [[" " for _ in range(8)] for _ in range(8)]
        return tabuleiro

    def mostrar_tabuleiro(self):
        for linha in self.tabuleiro:
            print(" ".join(linha))

    def obter_fen(self):
        board = chess.Board()
        for i in range(8):
            for j in range(8):
                peca = self.tabuleiro[i][j]
                if peca != " ":
                    board.set_piece_at(chess.square(j, 7 - i), chess.Piece.from_symbol(
                        peca[0].lower() if peca.cor == "preto" else peca[0].upper()))
        return board.fen()


class JogoXadrez:
    def __init__(self):
        self.tabuleiro = Tabuleiro()

    def jogar(self):
        while True:
            self.tabuleiro.mostrar_tabuleiro()
            movimento = input("Digite seu movimento: ")
            print(f"Você digitou: {movimento}")

            fen = self.tabuleiro.obter_fen()
            melhor_jogada = obter_melhor_jogada(fen)
            print(f"Melhor jogada sugerida: {melhor_jogada}")

            break


if __name__ == "__main__":
    jogo = JogoXadrez()
    jogo.jogar()
