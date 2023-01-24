from flask import Flask

app = Flask(__name__)

@app.route("/")
def home(name=None):
    return render_template('hello.html', name=name)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)