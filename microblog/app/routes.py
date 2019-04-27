from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Sameer'}
    posts = [
        {
            'author': {'username' : 'joe'},
            'body': 'Beautiful day in toronto'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }

    ]
    
    
    return render_template('index.html', title='Home', user=user, posts=posts)


