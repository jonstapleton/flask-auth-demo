from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/view-materials")
def view_materials():
    return render_template('view-materials.html')

@app.route("/submit-material", methods=["POST"])
def submit():
    first_name = request.form["first_name"]
    email = request.form["email"]
    print(f"Got POST request from {first_name} with email {email}")
    return "form submitted"

@app.route("/add-material")
def add_material():
    return render_template("form.html")