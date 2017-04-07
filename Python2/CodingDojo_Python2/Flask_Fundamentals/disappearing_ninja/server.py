from flask import Flask, redirect, render_template, session
app = Flask(__name__)

app.secret_key = "ThisIsSecret"



@app.route("/")
def index():

    return render_template("index.html")

@app.route("/show")
def show():
    flag = True

    return render_template("show.html",flag=flag)

@app.route("/ninja/<turtle>")
def ninja(turtle):
    flag = False

    return render_template("show.html", turtle=turtle, flag=flag)


app.run(debug=True)
