
from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html", title="Home")

@app.route("/about")
def about():
    return "About Page!"
