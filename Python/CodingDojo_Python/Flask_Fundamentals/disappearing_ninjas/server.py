from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def no_ninja():
    # add code here
    return render_template("index.html")

@app.route('/ninja')
def all_ninja():
    flag = True
    # add code here

    return render_template("ninja.html",flag=flag)

@app.route('/ninja/<turtle>')
def blue_ninja(turtle):
    flag = False
    # add code here

    return render_template("ninja.html",turtle=turtle,flag=flag)



app.run(debug=True)
