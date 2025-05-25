from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, mundo! Flask na AWS!"

@app.route("/transacao")
def home():
    return "Olá, mundo! Aqui será as transações!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
