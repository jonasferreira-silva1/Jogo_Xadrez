from flask import Flask, request, jsonify, send_from_directory
from robo import obter_melhor_jogada, obter_dica_educativa
import os

app = Flask(__name__, static_folder=".")


@app.route("/melhor_jogada", methods=["POST"])
def melhor_jogada():
    data = request.json
    fen = data["fen"]
    melhor_jogada = obter_melhor_jogada(fen)
    return jsonify({"melhor_jogada": melhor_jogada})


@app.route("/dica_educativa", methods=["POST"])
def dica_educativa():
    data = request.json
    fen = data["fen"]
    resultado = obter_dica_educativa(fen)
    return jsonify(resultado)


# Rota para servir a página inicial
@app.route("/")
def index():
    return send_from_directory('.', 'index.html')


# Rota para servir arquivos estáticos
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory('.', path)


if __name__ == "__main__":
    app.run(debug=True)
