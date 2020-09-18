from flask import Flask, render_template, request, flash, redirect, url_for, session, send_from_directory
import os
from dotenv import load_dotenv
from .forms import LoginForm, UploadForm, ContentForm
import click
from .models import Content, User


from . import create_app
app = create_app('development')


dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm(meta={'locales': ['zh']})
    if form.validate_on_submit():
        username = form.username.data
        print(form.password.data)
        flash(f'welcome home {username}')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
        flash('Upload success!')
        session['filename'] = [f.filename]
        return redirect(url_for('get_file', filename=f.filename))
    return render_template('upload.html', form=form)


@app.route('/uploads')
def get_file():
    filename = request.args.get('filename')
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@app.route('/content', methods=['GET', 'POST'])
def content():
    form = ContentForm()
    ct = Content.query.all()
    return render_template('content.html', cts=ct, form=form)
