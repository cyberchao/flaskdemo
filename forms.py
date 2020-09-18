from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

    # 自定义验证器，行内验证器
    def validate_username(form, field):
        if field.data != 'jiachao':
            raise ValidationError('名字必须是jiachao！')


class ContentForm(FlaskForm):
    content = StringField('文本', validators=[DataRequired(), Length(8, 300)])
    submit = SubmitField('send')


class UploadForm(FlaskForm):
    photo = FileField('upload image', validators=[
                      FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField()
