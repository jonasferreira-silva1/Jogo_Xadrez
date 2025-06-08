import chess
import chess.engine
import os
import random
import platform


def get_stockfish_path():
    """Tenta encontrar o caminho do Stockfish ou retorna None se não encontrado"""
    # Caminhos comuns para o Stockfish em diferentes sistemas operacionais
    possible_paths = []

    if platform.system() == "Windows":
        possible_paths = [
            "stockfish/stockfish-windows-x86-64.exe",  # Relativo ao diretório atual
            "stockfish.exe",  # Relativo ao diretório atual
            os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "stockfish", "stockfish-windows-x86-64.exe"),
            "C:/Program Files/Stockfish/stockfish.exe",
            "C:/Stockfish/stockfish.exe"
        ]
    elif platform.system() == "Linux":
        possible_paths = [
            "stockfish/stockfish-ubuntu-x86-64",
            "stockfish",
            "/usr/games/stockfish",
            "/usr/local/bin/stockfish"
        ]
    elif platform.system() == "Darwin":  # macOS
        possible_paths = [
            "stockfish/stockfish-macos-x86-64",
            "stockfish",
            "/usr/local/bin/stockfish"
        ]

    for path in possible_paths:
        if os.path.isfile(path):
            return path

    return None


def obter_melhor_jogada(fen):
    stockfish_path = get_stockfish_path()

    # Se o Stockfish estiver disponível, use-o
    if stockfish_path:
        try:
            engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
            board = chess.Board(fen)
            resultado = engine.play(board, chess.engine.Limit(time=0.1))
            engine.quit()
            return resultado.move.uci()
        except Exception as e:
            print(f"Erro ao usar o Stockfish: {e}")
            # Continua para a versão simulada

    # Versão simulada quando o Stockfish não está disponível
    try:
        board = chess.Board(fen)
        movimentos_legais = list(board.legal_moves)
        if movimentos_legais:
            # Escolhe um movimento aleatório
            movimento = random.choice(movimentos_legais)
            return movimento.uci()
        return ""
    except Exception as e:
        print(f"Erro ao gerar movimento simulado: {e}")
        return ""


def obter_dica_educativa(fen):
    stockfish_path = get_stockfish_path()

    # Se o Stockfish estiver disponível, use-o
    if stockfish_path:
        try:
            engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
            board = chess.Board(fen)

            # Obter a melhor jogada
            resultado = engine.play(board, chess.engine.Limit(time=0.1))
            melhor_jogada = resultado.move

            # Analisar a posição antes e depois da jogada
            info_antes = engine.analyse(board, chess.engine.Limit(depth=15))
            board.push(melhor_jogada)
            info_depois = engine.analyse(board, chess.engine.Limit(depth=15))

            # Determinar o tipo de jogada e gerar uma dica educativa
            dica = gerar_dica_baseada_na_jogada(
                board, melhor_jogada, info_antes, info_depois)

            engine.quit()
            return {
                "jogada": melhor_jogada.uci(),
                "dica": dica,
                "avaliacao": info_antes["score"].white().score(mate_score=10000) / 100
            }
        except Exception as e:
            print(f"Erro ao usar o Stockfish para dica educativa: {e}")
            # Continua para a versão simulada

    # Versão simulada quando o Stockfish não está disponível
    try:
        board = chess.Board(fen)
        movimentos_legais = list(board.legal_moves)

        if not movimentos_legais:
            return {
                "jogada": "",
                "dica": "Não há movimentos legais disponíveis.",
                "avaliacao": 0
            }

        # Escolhe um movimento aleatório
        melhor_jogada = random.choice(movimentos_legais)

        # Verifica se é uma captura ou xeque
        board.push(melhor_jogada)
        xeque = board.is_check()
        captura = board.is_capture(melhor_jogada)

        # Determina o tipo de dica
        if xeque:
            dica_tipo = "xeque"
        elif captura:
            dica_tipo = "captura"
        elif melhor_jogada.to_square in [27, 28, 35, 36]:  # Casas centrais
            dica_tipo = "centro"
        else:
            dica_tipo = random.choice(["desenvolvimento", "defesa", "geral"])

        # Obtém a dica correspondente
        dicas = {
            "desenvolvimento": "Desenvolva suas peças no início do jogo para controlar o centro do tabuleiro.",
            "captura": "Bom movimento! Capturar peças do oponente quando vantajoso ajuda a ganhar material.",
            "xeque": "Xeque! Colocar o rei adversário em xeque força seu oponente a responder à ameaça.",
            "defesa": "Este movimento protege suas peças importantes de ameaças imediatas.",
            "centro": "Controlar o centro do tabuleiro dá mais opções de movimento e aumenta sua influência.",
            "geral": "Pense sempre alguns lances à frente e considere o que seu oponente pode fazer."
        }

        return {
            "jogada": melhor_jogada.uci(),
            "dica": dicas[dica_tipo],
            "avaliacao": random.uniform(-2.0, 2.0)  # Avaliação simulada
        }
    except Exception as e:
        print(f"Erro ao gerar dica simulada: {e}")
        return {
            "jogada": "",
            "dica": "Não foi possível analisar a posição atual.",
            "avaliacao": 0
        }


def gerar_dica_baseada_na_jogada(board, jogada, info_antes, info_depois):
    # Identificar o tipo de jogada
    peca_movida = board.piece_at(jogada.to_square)
    captura = board.is_capture(jogada)
    xeque = board.is_check()

    dicas = {
        # Dicas para desenvolvimento de peças
        "desenvolvimento": "Desenvolva suas peças no início do jogo para controlar o centro do tabuleiro.",

        # Dicas para capturas
        "captura": "Bom movimento! Capturar peças do oponente quando vantajoso ajuda a ganhar material.",

        # Dicas para xeque
        "xeque": "Xeque! Colocar o rei adversário em xeque força seu oponente a responder à ameaça.",

        # Dicas para defesa
        "defesa": "Este movimento protege suas peças importantes de ameaças imediatas.",

        # Dicas para controle do centro
        "centro": "Controlar o centro do tabuleiro dá mais opções de movimento e aumenta sua influência.",

        # Dica genérica
        "geral": "Pense sempre alguns lances à frente e considere o que seu oponente pode fazer."
    }

    # Lógica para escolher a dica apropriada
    if xeque:
        return dicas["xeque"]
    elif captura:
        return dicas["captura"]
    elif peca_movida and peca_movida.piece_type in [chess.PAWN, chess.KNIGHT, chess.BISHOP] and board.fullmove_number < 10:
        return dicas["desenvolvimento"]
    # Casas centrais (d4, e4, d5, e5)
    elif jogada.to_square in [27, 28, 35, 36]:
        return dicas["centro"]
    else:
        return dicas["geral"]
