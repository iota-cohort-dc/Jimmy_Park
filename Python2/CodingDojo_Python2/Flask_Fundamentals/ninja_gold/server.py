from flask import Flask, render_template, session, redirect
app = Flask(__name__)

@app.route()
def index():

    if "activity" in session:
        pass
    else:
        session['activity'] = []

    if "gold" in session:
        pass
    else:
        session['gold'] = 0

    return render_template("/")

@app.route()
def goldgame():

    

    return render_template("/")

app.run(debug=True)
