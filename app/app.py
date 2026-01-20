from flask import Flask, render_template

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

