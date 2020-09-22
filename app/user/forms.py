from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed
from .models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(2, 20)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(2, 128)])
    password_sub = PasswordField('Password_sub', validators=[
        DataRequired(), Length(2, 128), EqualTo('password')])
    email = StringField('email', validators=[
        DataRequired(), Length(5, 128)])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.')

    # 自定义验证器，行内验证器
    # def validate_username(form, field):
    #     if field.data != 'jiachao':
    #         raise ValidationError('名字必须是jiachao！')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(2, 20)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
