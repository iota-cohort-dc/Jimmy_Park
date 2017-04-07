from flask import Flask, redirect, render_template
app.Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/show")
def show():

    
    return render_template("show.html")

app.run(debug=True)
