from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "burrito"

@app.route('/') # url from browser matches to this route
def index(): # define method function to apply logic to route

    # print session # inspecting session variable
    if "counter" in session: # is the counter key in the session dictionary
        # if it is, plus one to it
        session['counter'] += 1
        
    else:
        # if not, set key counter in session to 0
        session['counter'] = 0

    return render_template("index.html") # get and render the index html file

@app.route('/count', methods=["POST"])
def counter():

    session['counter'] += 1

    return redirect('/')

@app.route('/reset')
def reset():

    session['counter'] = 0
    return redirect('/')
app.run(debug=True) # run our server
