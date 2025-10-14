from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Material:
    # define class variables
    name="Default Name"
    cost=0.00
    description="A default description to display on the screen."
    quantity=0
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

@app.route("/materials")
def view_materials():
    return render_template('view-materials.html', materials=d)
