from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route("/")
def homepage():

    print dir(request)

    return render_template


app.run(debug=True)
