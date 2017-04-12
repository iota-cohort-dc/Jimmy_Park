from flask import Flask, render_template, redirect, session, request
from random import randint

app = Flask(__name__)
app.secret_key = "jimmy"
import random

@app.route('/')
def index():
    #input if statement

    if 'activity' in session:
        pass
    else:
        session['activity'] = []

    if 'gold' in session:
        pass
    else:
        session['gold'] = 0

    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    #input if statement
    if request.form['building'] == "farm":
        print "at the house ************"
        session['gold'] += randint(12,20)
        prnt_farm_actvty = "You got " + str(session['gold']) + " gold coins from the farm."
        session['activity'].append(prnt_farm_actvty)
        # print session['gold']


    if request.form['building'] == "cave":
        print "at the cave ************"
        session['gold'] += randint(5,10)
        prnt_cave_actvty = "You got " + str(session['gold']) + " gold coins from the farm."
        session['activity'].append(prnt_cave_actvty)
        # print session['gold']

    if request.form['building'] == "house":
        print "at the house ************"
        session['gold'] += randint(2,5)
        prnt_house_actvty = "You got " + str(session['gold']) + " gold coins from the farm."
        session['activity'].append(prnt_house_actvty)
        # print session['gold']

    if request.form['building'] == "casino":
        print "at the casino ************"
        session['gold'] += randint(-50,50)
        prnt_casino_actvty = "You got " + str(session['gold']) + " gold coins from the farm."
        session['activity'].append(prnt_casino_actvty)
        # print session['gold']

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    print "Your session has been terminated"
    return redirect('/')

app.run(debug=True) # run our server

# session['']
# return redirect('/')
# return render_template('/')
# (request.form['name from input html']
# @app.route('/process', methods=['POST'])
#
