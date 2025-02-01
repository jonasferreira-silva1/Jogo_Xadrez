import tkinter as tk
from pecas import Rei, Rainha, Torre, Bispo, Cavalo, Peao

class JogoXadrez:
    def __init__(self, master):
        self.master = master
        self.master.title("Xadrez")
        self.tabuleiro = tk.Canvas(self.master, width=600, height=600)
        self.tabuleiro.pack()
        self.estado_inicial = self.inicializar_tabuleiro()
        self.desenhar_tabuleiro()
        self.peca_selecionada = None

    def inicializar_tabuleiro(self):
        return [
            [Torre("preto"), Cavalo("preto"), Bispo("preto"), Rainha("preto"), Rei("preto"), Bispo("preto"), Cavalo("preto"), Torre("preto")],
            [Peao("preto"), Peao("preto"), Peao("preto"), Peao("preto"), Peao("preto"), Peao("preto"), Peao("preto"), Peao("preto")],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Peao("branco"), Peao("branco"), Peao("branco"), Peao("branco"), Peao("branco"), Peao("branco"), Peao("branco"), Peao("branco")],
            [Torre("branco"), Cavalo("branco"), Bispo("branco"), Rainha("branco"), Rei("branco"), Bispo("branco"), Cavalo("branco"), Torre("branco")]
        ]

    def desenhar_tabuleiro(self):
        for i in range(8):
            for j in range(8):
                cor = "white" if (i + j) % 2 == 0 else "gray"
                self.tabuleiro.create_rectangle(j * 75, i * 75, (j + 1) * 75, (i + 1) * 75, fill=cor)
                peca = self.estado_inicial[i][j]
                if peca:
                    peca_id = self.tabuleiro.create_text(j * 75 + 37.5, i * 75 + 37.5, text=peca.__class__.__name__[0], font=("Arial", 24, "bold"), fill=peca.cor)
                    self.tabuleiro.tag_bind(peca_id, "<Button-1>", lambda event, i=i, j=j: self.selecionar_peca(event, i, j))

    def selecionar_peca(self, event, linha, coluna):
        if not self.peca_selecionada:
            self.peca_selecionada = (linha, coluna)
        else:
            linha_origem, coluna_origem = self.peca_selecionada
            self.estado_inicial[linha][coluna] = self.estado_inicial[linha_origem][coluna_origem]
            self.estado_inicial[linha_origem][coluna_origem] = None
            self.peca_selecionada = None
            self.tabuleiro.delete("all")
            self.desenhar_tabuleiro()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoXadrez(root)
    root.mainloop()
