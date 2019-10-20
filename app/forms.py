from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, IntegerField
from app import app


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.input_required()])
    password = PasswordField('Password', [validators.input_required()])
    multifa = IntegerField("2FA - Phone Number", [validators.optional()])
    remember_me = BooleanField('Remember Me', [validators.optional()])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.input_required()])
    password = PasswordField('Password', [validators.input_required()])
    multifa = IntegerField("2FA - Phone Number", [validators.optional()])
    submit = SubmitField('Sign Up')


class SpellChecker(FlaskForm):
    command = StringField('Spell check words input', [validators.input_required()])
