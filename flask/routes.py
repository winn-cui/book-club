from fw import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Winn'}
    return render_template('index.html', title='Home', user=user)


@app.route('/library')
@app.route('/')  
