from flask import Flask, render_template

app = Flask(__name__)

def suma(a, b):
    return a + b

@app.route("/")
def home():
    resultado = suma(2, 3)
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)