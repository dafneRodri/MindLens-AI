from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route("/")
def login():
    return render_template("login.html")

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)