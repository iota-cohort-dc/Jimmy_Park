from flask import Flask, render_template, request, redirect, session
# import random
app = Flask(__name__)
app.secret_key = "jimmy"
import random

@app.route('/') # url from browser matches to this route
def index(): # define method function to apply logic to route

    if "random_num" in session: # is the counter key in the session dictionary
        pass # if the random_num DOES have a number it will pass the (else).
    else:
        session['random_num'] = random.randrange(1,100) # setting the session['random_num'] with random number
    print session['random_num']

    return render_template("index.html") # get and render the index html file

@app.route('/process', methods=['POST'])
def highorlow():

    print session # prints to the terminal, helps to see where you are at
    # int - is intager, ['number'] is targeting form/input/name in html
    guess = int(request.form['number']) #targeting the name in the html
    print "*******************************"

    if guess < session['random_num']:
        print guess # prints to the terminal, helps to see where you are at
        session['hilo'] = "Too Low, Try Again" # seting session value
        print session['hilo'] # pointing to {{ hilo }} in the html
        return render_template('index.html', highlow = "Too Low!, Try Again!")

    elif guess > session['random_num']:
        print guess # prints to the terminal, helps to see where you are at
        session['hilo'] = "Too High, Try Again" # setting session value
        print session ['hilo'] # pointing to {{ hilo }} in the html
        return render_template('index.html', highlow = "Too High!, Try Again!")

    elif guess == session['random_num']:
        print "Winner !!!!!!!!!!!!!!!!!!!!!!!!"
        return render_template('congrats.html') # reloads to another html doc

@app.route('/reset', methods=['POST']) # /reset is from the forms/action/reset
def reset():
    session.clear() # clears the cache so it erases the stored number
    return redirect('/') # redirects you to the index.html

app.run(debug=True) # run our server
