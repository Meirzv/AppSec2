from flask import render_template, flash, redirect, request
from app import app
from app.forms import LoginForm, RegisterForm

programMemory = dict()  #


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.username.data.lower() in programMemory.keys():
            flash("Username must be unique. '" + form.username.data+"' is not available. ")
            return redirect('/register')
        else:
            programMemory[form.username.data.lower()] = [form.password.data,form.username.data]
            flash("Successful")
            for element in programMemory.keys():
                print(element)
            return redirect('/index')
    else:
        return render_template('register.html', title='Sign Up', form=form)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')
