from flask_login import UserMixin
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash

db.create_all()


class LoginUser(db.Model, UserMixin):
    __tablename__ = 'user'

    username = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    mfa = db.Column(db.String(80), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    pw_hash = db.Column(db.String)

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


# class User(db.Model):
#     username = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
#     _2fa = db.Column(db.String(80), nullable=False)
#
#     def set_password(self, password):
#         self.password = generate_password_hash(password)
#
#     def get_password(self, password):
#         return check_password_hash(self.password, password)
