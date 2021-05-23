#!/usr/bin/env python3
#"""Basic Hello world app""

from flask import Flask # from the flask package import flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello world!</h1>"
@app.route("/about")
def about():
    me = {
        "first_name":"Johnny",
        "last_name": "Jimenez",
        "hobbies": "DIY stuff, mechanic",
        "ok":"True"
    }
    return me