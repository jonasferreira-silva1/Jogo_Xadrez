import chess
import chess.engine

def obter_melhor_jogada(fen):
    engine = chess.engine.SimpleEngine.popen_uci("path/to/stockfish")  # Certifique-se de ter o Stockfish instalado e acessível
    board = chess.Board(fen)
    resultado = engine.play(board, chess.engine.Limit(time=0.1))
    engine.quit()
    return resultado.move.uci()
