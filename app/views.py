from flask import render_template, flash, redirect, request
from app import app
from app.forms import LoginForm, RegisterForm, SpellChecker

programMemory = dict()  # [key = lower key username. value = 1) password, 2) original username, 3) 2fa]


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data.lower() in programMemory.keys():
            if form.password.data == programMemory[form.username.data.lower()][0]:
                flash("Login is successful ")
                return redirect('/spell_check')
            else:
                flash("Password is incorrect. Please try again")
                return redirect('/login')
        else:
            flash("Username is incorrect. Please try again")
            return redirect('/login')
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.username.data.lower() in programMemory.keys():
            flash("Username must be unique. '" + form.username.data + "' is not available. ")
            return redirect('/register')
        else:
            programMemory[form.username.data.lower()] = [form.password.data, form.username.data, form.multifa.data]
            flash("Successful")
            for element in programMemory.keys():
                print(element)
            return redirect('/index')
    else:
        return render_template('register.html', title='Sign Up', form=form)


@app.route('/spell_check')
def spell_checker():
    form = SpellChecker()
    return render_template('spell_check.html', title="Spell Check App", form=form)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')
