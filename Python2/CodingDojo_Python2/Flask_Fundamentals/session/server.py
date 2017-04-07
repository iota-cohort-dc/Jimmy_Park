from flask import Flask, redirect, render_template, session
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/session")
def session():
    pass

app.run(debug=True)
