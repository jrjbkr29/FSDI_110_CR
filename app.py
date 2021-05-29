#!/usr/bin/env python3
#"""Basic Hello world app""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from database import User

@app.route("/index")
def hello():
    return render_template("index.html")

@app.route("/about")
def about():
    me = {
        "first_name":"Johnny",
        "last_name": "Jimenez",
        "hobbies": "Working on cars",
        "ok":"True"
    }
    return render_template("about.html", user=me)

@app.route("/about/<int:uid>")
def about_user(uid):
    user = User.query.filter_by(id=uid).first()
    return render_template("about.html", user=user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404