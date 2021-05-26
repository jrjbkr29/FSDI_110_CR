#!/usr/bin/env python3
#"""Basic Hello world app""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQL_ALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from database import User

@app.route("/")
def hello():
    return render_template("home.html")
@app.route("/about")
def about():
    me = {
        "first_name":"Johnny",
        "last_name": "Jimenez",
        "hobbies": "DIY stuff, mechanic",
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