from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm    

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

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
