from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #localhost:5000/success <--

def world(): #function name
    return render_template('index.html') #in () file dirctory


@app.route('/ninja') #localhost:5000/success <--

def ninja_world(): #function name
    return render_template('ninjas.html') #in () file dirctory


@app.route('/dojo/new') #localhost:5000/success <--

def dojo_world(): #function name
    return render_template('dojo.html') #in () file dirctory

app.run(debug=True)
