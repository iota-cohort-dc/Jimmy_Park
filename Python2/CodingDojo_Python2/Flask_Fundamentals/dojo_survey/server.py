from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/result", methods=['POST'])
def result():

    names = request.form['name']
    locate = request.form['location']
    favorite = request.form['favLang']
    comm = request.form['comment']

    # print names
    # print locate
    # print favorite
    # print comm

    return render_template("result.html",names=names,locate=locate,favorite=favorite,comm=comm)

app.run(debug=True)
