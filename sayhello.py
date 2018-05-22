from flask import Flask, render_template
from flask import abort


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    comments = list('qwertyuighgj')
    return render_template('user.html',comments=comments, user=True, name=name)


if __name__ == '__main__':
    app.run(debug=True)