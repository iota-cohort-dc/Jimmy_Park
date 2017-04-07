from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html", phrase="hello", times=5)

app.run(debug=True)
