from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def homepage():

    print dir(request) # print all

    return render_template("index.html")# ,pullname = pullname

@app.route("/samepage", methods=['POST'])
def nextpage():

    pullname = request.form['name']

    return render_template("index.html", pullname = pullname)

# @app.route("/samepage", methods=['POST']) ## use this to go to another index page
# def nextpage(): ## use this to go to another index page
#
#     pullname = request.form['name']  ## use this to go to another index page
#
#     return render_template("next.html", pullname = pullname) ## use this to go to another index page

app.run(debug=True)
