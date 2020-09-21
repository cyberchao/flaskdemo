from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ContentForm(FlaskForm):
    content = StringField('文本', validators=[DataRequired(), Length(1, 300)])
    submit = SubmitField('send')

class CommentForm(FlaskForm):
    content = StringField('评论', validators=[DataRequired(), Length(1, 300)])
    submit = SubmitField('send')

class UploadForm(FlaskForm):
    photo = FileField('upload image', validators=[
                      FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField()
