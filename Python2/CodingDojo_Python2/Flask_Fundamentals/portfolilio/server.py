from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route("/")
def homepage():

    print dir(request)

    return render_template("index.html")

@app.route("/projects")
def projects():

    print dir(request)

    return render_template("projects.html")

@app.route("/about")
def about():

    print dir(request)

    return render_template("about.html")


app.run(debug=True)
