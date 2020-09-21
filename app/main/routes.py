from flask import render_template, Blueprint
from demo.app.posts.forms import ContentForm,CommentForm
from demo.app.posts.models import Content,Comment

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    form = ContentForm()
    cmform = CommentForm()
    ct = Content.query.order_by(Content.date.desc())
    return render_template('index.html', cts=ct, form=form,cmform=cmform)
