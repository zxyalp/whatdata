from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = ' hand to guess string'


@app.route('/', methods=('GET', 'POST'))
def hello_world():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=name)


@app.route('/user/<name>')
def user(name):
    comments = list('qwertyuighgj')
    return render_template('user.html', comments=comments, user=True, name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class UserForm(FlaskForm):
    name = StringField('姓名：', validators=[DataRequired()])
    submit = SubmitField('提交')


if __name__ == '__main__':
    app.run(debug=True)