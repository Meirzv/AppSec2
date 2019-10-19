from app import app


# from flask import Flask, request, render_template
# from wtforms import Form, StringField, validators
# #from flask_login import LoginManager, current_user, login_required, logout_user, login_user
#
#
# app = Flask(__name__)
#
#
# #login_manager = LoginManager(app)
# #login_manager.init_app(app)
#
#
# @app.route('/')
# def index():
#     print(request.method)
#     print(request.headers)
#     return render_template('index.html')
#
#
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#     return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run()
