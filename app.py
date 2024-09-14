from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from flask_font_awesome import FontAwesome

app = Flask(__name__)
font_awesome = FontAwesome(app)
app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    session["username"] = username
    return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
