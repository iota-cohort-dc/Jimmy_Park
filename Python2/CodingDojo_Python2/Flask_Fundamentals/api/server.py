from flask import Flask, session, redirect, render_template
app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/show/image/<id>")
def show(id):
    session = session.GET['name']

    return render_template("show.html")

app.run(debug=True)
