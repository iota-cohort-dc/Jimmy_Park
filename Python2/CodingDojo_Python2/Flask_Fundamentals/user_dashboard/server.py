from flask import Flask, redirect, render_template, session, flash
app = Flash(__name__)
app.secret_key = "jimmy"
import random

@app.route("/")
def index():
    print "*" *30
    return render_template("index.html")

@app.route("/")
def index():
    print "*" *30
    return render_template("index.html")
app.run(debug=True)
