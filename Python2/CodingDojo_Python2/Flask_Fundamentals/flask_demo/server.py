from flask import Flask,render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])# can also ['POST','GET']
def homepage():

    print dir(request) # print all
    # print request.values['myfirstdata']
    print request.form['myfirstdata']

    return render_template("index.html")

@app.route('/pkp', methods=['POST'])
def newfunction():

    print "your a noob"

    return render_template("nextpage.html")

app.run(debug=True)
