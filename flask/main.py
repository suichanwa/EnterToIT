from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username', 'some'}
    return render_template('hello.html', title ='Home', user=user)

