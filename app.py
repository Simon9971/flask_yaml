from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/form')
def form():
    if request.method == 'POST':
        name = request.form['name']


if __name__ == '__main__':
    app.run()
