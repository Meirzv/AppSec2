from flask import render_template, redirect, url_for, flash, request, Markup
from flask_login import LoginManager, current_user, login_required, logout_user, login_user
import subprocess

from app import app, db, models
from app.forms import LoginForm, RegisterForm, SpellChecker
from app.models import LoginUser
import os

basedir = os.path.abspath(os.path.dirname(__file__))
login_manager = LoginManager(app)
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(user_id):
    print("LOADING USER FOR " + user_id)
    return models.LoginUser.query.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('spell_checker'))
    form = LoginForm()
    if form.validate_on_submit():
        user = models.LoginUser.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(Markup('Invalid username or password <li class="meir" id="result"> incorrect Username/password or Two-factor failure </li>'))
            print("INVALID")
            return redirect(url_for('login'))
        login_user(user)
        flash(Markup('Logged in successfully. <li class="meir" id="result"> success </li>'))
        return redirect(url_for('spell_checker'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = models.LoginUser(username=form.username.data, mfa=form.mfa.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(Markup('Congratulations, you are now a registered user! <li class="meir" id="success"> success </li>'))
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    else:
        flash(Markup('Something went wrong. Please try to register again <li class="meir" id="success"> failure </li>'))
        return render_template('register.html', title='Sign Up', form=form)


@app.route('/spell_check', methods=['GET', 'POST'])
def spell_checker():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = SpellChecker()
    print("okay so far1")
    if form.validate_on_submit():
        print("okay so far")
        p1 = subprocess.Popen("echo " + form.command.data + " > words.txt", shell=True)
        p1.wait()
        p2 = subprocess.Popen(basedir + '/a.out words.txt wordlist.txt', stdin=None, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p3 = p2.stdout
        output = list()
        for words in p3:
            words = words.decode("utf-8").split()
            for word in words:
                output.append(word)

        print("this is the output " + str(output))
        #print(*output, sep=', ')
        flash(Markup('Misspelled words are: <li class="meir" id="textout">' + str(output) + ' </li>'))
        return redirect(url_for('spell_checker'))
    else:
        return render_template('spell_check.html', title="Spell Check App", form=form)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('index')
