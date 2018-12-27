from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Isaac'}
    posts = [
        {
            'author':{'username':'John'},
            'body':'Beautiful day in Gunnison!'
        }, 
        {
            'author':{'username':'Susan'},
            'body': 'The Avengers movie is in theaters!'
        }, 
        {
            'author':{'username':'James'},
            'body': 'I have added another post!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    