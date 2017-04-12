from flask import Flask, redirect, render_template, session, request
import random
app = Flask(__name__)
app.secret_key = "jimmy"

@app.route("/")
def index():

    if "random_number" in session:
        pass
        print " ************************"
    else:
        session["random_number"] = random.randrange(0,100)
        print " ************************"

    print session['random_number']

    return render_template("index.html")

@app.route("/guessgame", methods=["POST"])
def guessgame():

    # print "** ** ** ** ** ** ** ** ** "
    guess = int(request.form['guess']) #set the variable at the top..
    # print "++++++++++++++++++++++++++"

    if guess < session["random_number"]:
        highlow = "Too LOW, Try Again"

        return render_template('index.html', highlow = highlow, guess=guess)

    elif guess > session["random_number"]:
        highlow = "Too HIGH, Try Again"

        return render_template('index.html', highlow = highlow, guess=guess)

    elif guess == session["random_number"]:
        congrats = "Congrats, You've Won $1,000,000"
        return render_template('index.html', congrats = congrats, guess=guess)

    return render_template("index.html", guess=guess)

@app.route("/success")
def reset():
    session.clear()
    pass

    return render_template("success.html")

app.run(debug=True)
