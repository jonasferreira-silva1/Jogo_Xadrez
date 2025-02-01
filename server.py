from flask import Flask, request, jsonify
from robo import obter_melhor_jogada

app = Flask(__name__)

@app.route("/melhor_jogada", methods=["POST"])
def melhor_jogada():
    data = request.json
    fen = data["fen"]
    melhor_jogada = obter_melhor_jogada(fen)
    return jsonify({"melhor_jogada": melhor_jogada})

if __name__ == "__main__":
    app.run(debug=True)
