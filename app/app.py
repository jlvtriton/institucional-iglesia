from flask import Flask, render_template, jsonify
from app.textos_biblicos import BIBLIA_RVR

app = Flask(__name__)   # 👈 AQUÍ se define la app


@app.route("/")
def inicio():
    return render_template("manual/inicio.html")

@app.route("/vision")
def vision():
    return render_template("manual/vision.html")

@app.route("/mision")
def mision():
    return render_template("manual/mision.html")

@app.route("/valores")
def valores():
    return render_template("manual/valores.html")

@app.route("/manual")
def manual():
    return render_template("manual/manual.html")

@app.route("/puntos_doctrinales")
def puntos_doctrinales():
    return render_template("manual/puntos_doctrinales.html")

@app.route("/biblia/<clave>")
def obtener_texto_biblico(clave):
    texto = BIBLIA_RVR.get(clave)
    if texto:
        return jsonify(texto)
    return jsonify({"texto": "Texto no encontrado", "version": ""})