from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, IntegerField
# from .util.validators import Unique
# from app.views import programMemory


class LoginForm(FlaskForm):
    username = StringField('Username',  [validators.input_required()])
    password = PasswordField('Password', [validators.input_required()])
    multifa  = IntegerField("2FA - Phone Number")
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username',  [validators.input_required()])
    password = PasswordField('Password', [validators.input_required()])
    multifa  = IntegerField("2FA - Phone Number", [validators.optional()])
    submit = SubmitField('Sign Up')