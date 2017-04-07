from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route("/")
def index():

    # print dir(request)


    return render_template("index.html")

@app.route("/ninjas")
def ninjas():

    # print dir(request)

    print "*********************"

    return render_template("ninjas.html")

@app.route("/dojos")
def dojoNew():

    # print dir(request)

    print "*********************"
    return render_template("dojos.html")


app.run(debug=True)
