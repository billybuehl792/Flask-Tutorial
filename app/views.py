
import re
from app import app
from flask import render_template, request, redirect, jsonify, make_response
from datetime import datetime

users = {
    "bbuehl792" : {
        "name": "Billy Buehl",
        "bio": "Motion Designer",
        "site": "instagram.com/kevinjosephcole_art"
    }, 
    "duncanM1" : {
        "name": "Duncan McDonell",
        "bio": "Uran Planner",
        "site": "trains.com"
    }, 
    "gooberH7" : {
        "name": "Christian Hutchinson",
        "bio": "Goober",
        "site": "smirnoff.com"
    }, 
}

@app.template_filter('clean_date')
def clean_date(dt):
    return dt.strftime('%d %b %Y')

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():
    
    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.desctiption = description
            self.url = url

        def pull(self):
            return f"Pulling repo: {self.name}"

        def clone(self):
            return f"Cloning repo: {self.url}"

    def repeat(v, m):
        return v * m

    my_name = "Billy"
    age = 25
    langs = ["Python", "Javascript"]
    friends = {
        "Billy": 25,
        "Hannah": 21,
        "Duncan": 25,
        "Charlie": 25
    }

    cool = True
    colors = ("Red", "Green")
    date = datetime.utcnow()
    
    my_remote = GitRemote(
        name="Flask Jinja",
        description="Flask training stuff",
        url="https://github.com/billybuehl792/Flask-Tutorial"
    )

    my_html = "<h1>my html is this</h1>"

    return render_template(
        "public/jinja.html", my_name=my_name, age=age, langs=langs,
        my_remote=my_remote, GitRemote=GitRemote, friends=friends, 
        colors=colors, repeat=repeat, cool=cool, date=date, my_html=my_html
        )

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        req = request.form
        username = req.get("username")
        email = req.get("email")
        password = req.get("password")

        print(f"user: {username}, email: {email}, password: {password}")
        return redirect(request.url)
    
    return render_template("public/sign_up.html")

@app.route("/profile/<username>")
def profile(username):

    user = None

    if username in users:
        user = users[username]

    return render_template("public/profile.html", user=user, username=username)

@app.route("/json", methods=["GET", "POST"])
def json():

    if request.is_json:
        req = request.get_json()
        response = {
            "message": "JSON received!",
            "name": req.get("name")
        }
        res = make_response(jsonify(response), 200)
        return res
    else: 
        res = make_response(jsonify({"message": "No JSON"}), 400)

@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")

@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()
    print(req)

    return make_response(jsonify({"message": "JSON Received!"}, 200))