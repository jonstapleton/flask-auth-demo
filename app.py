from flask import Flask, render_template, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy.orm as so
import sqlalchemy as sa

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Material(db.Model):
    # define class variables
    id:so.Mapped[int] = so.mapped_column(primary_key = True)
    cost:so.Mapped[float] = so.mapped_column(index=True, default=0.00)
    description:so.Mapped[str] = so.mapped_column(index=True, default="A default description to display on the screen.")
    quantity:so.Mapped[int] = so.mapped_column(index=True, default=0)
    # write the constructor
    def __init__(self):
        pass

a = Material()
a.name = "Red Oak"
a.cost = 7.25

d = [ Material(), a ] # make a list with an object in it

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/materials", methods=["GET", "POST"])
def view_materials():
    if request.method == 'GET':
        # do GET stuff
        pass
    elif request.method == 'POST':
        # do post stuff, like store form field data
        print(f"Form submitted with name {request.form["name"]}")
        o = Material()
        o.name = request.form["name"]
        d.append(o) # add o to the list of Materials
    
    return render_template('view-materials.html', materials=d)
