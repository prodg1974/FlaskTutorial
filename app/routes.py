from flask import render_template
from app import app
    

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'paul','lastfour':'8888'}
    posts = [
        {
            'author': {'username':'John'},
            'body':'Beautiful day in New Orleans!'
        },
        {
            'author':{'username':'Susan'},
            'body':'Bills lost, oh well!'
        }
    ]
    #return render_template('index.html', title='Home', user=user)
    return render_template('index.html', title = 'Loop',user=user, posts=posts)
