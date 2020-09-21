from flask import render_template, Blueprint, flash, redirect, session, request, send_from_directory, url_for, abort,jsonify
from .forms import ContentForm, UploadForm,CommentForm
import os
from .models import Content,Comment
from flask import current_app
from flask_login import current_user
from demo import db


content_bp = Blueprint('posts', __name__)


@content_bp.route('/', methods=['GET', 'POST'])
def content():
    form = ContentForm()
    ct = Content.query.all()
    return render_template('content.html', cts=ct, form=form)

@content_bp.route('/comment/<id>', methods=['get','POST'])
def comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        print(2)
        comment = Comment(body=form.content.data, user=current_user,content=Content.query.get(id))
        print(comment)
        db.session.add(comment)
        db.session.commit()
        print(3)
        flash('Your comment has been created!', 'success')
        return redirect(url_for('main.index'))
    cm=Comment.query.filter_by(content=Content.query.get(id))
    response = []
    for c in cm:
        response.append(c.to_json())
    return jsonify(response)

@content_bp.route('/create', methods=['POST'])
def create():
    form = ContentForm()
    if form.validate_on_submit():
        content = Content(body=form.content.data, user=current_user)
        db.session.add(content)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))


@content_bp.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    content = Content.query.get_or_404(id)
    if content.user != current_user:
        abort(403)
    db.session.delete(content)
    db.session.commit()
    flash('Your content has been deleted!', 'success')
    return redirect(url_for('posts.detail', id=current_user.id))


@content_bp.route('/detail/<id>', methods=['GET'])
def detail(id):
    ct = Content.query.filter_by(user_id=id).order_by(Content.date.desc())
    return render_template('user_detail.html', cts=ct)


@content_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        f.save(os.path.join(current_app.config.get('UPLOAD_PATH'), f.filename))
        flash('Upload success!')
        session['filename'] = [f.filename]
        return redirect(url_for('get_file', filename=f.filename))
    return render_template('upload.html', form=form)


@content_bp.route('/uploads')
def get_file():
    filename = request.args.get('filename')
    return send_from_directory(current_app.config.get('UPLOAD_PATH'), filename)
