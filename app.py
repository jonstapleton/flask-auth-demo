from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import os
from typing import Optional
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy.orm as so
import sqlalchemy as sa

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'app.db')
app.secret_key = "a secret"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key = True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def set_password(self, new_password):
        self.password = generate_password_hash(new_password)

    def check_password(self, p):
        return check_password_hash(self.password, p)

@login.user_loader
def loader(id):
    return db.session.get(User, int(id))

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == "POST":
        if current_user.is_authenticated:
            return 'already logged in!'
        user = db.session.scalar(
            sa.select(User).where(User.email== request.form["email"])
        )
        if user is None or not user.check_password(request.form["password"]):
            return 'login failed!'
        login_user(user)
        return 'login succeeded!'
    return 'ugh'        

