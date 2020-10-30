import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    (ant) = 0
    (prox) = 1
    (limite) = 50
    (found) = 1
    (resultado) = "0,"

    while found <= limite:
        temp = prox + ant
        ant = prox
        prox = temp
        resultado += str (temp) + ","
        found = found + 1

    return(resultado)

if __name__ == "__main__":
    port = int(os.environ.get("port", 5000))
    app.run(host='0.0.0.0', port=port)
