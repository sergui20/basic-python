from flask import Flask

# Flask nos pide que enviemos el nombre del modulo
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, mundo...'


if __name__ == "__main__":
    app.run()    