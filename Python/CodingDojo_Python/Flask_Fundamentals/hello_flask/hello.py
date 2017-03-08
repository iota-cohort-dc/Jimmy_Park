from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #localhost:5000/success <--




def hello_world(): #function name
    return render_template('index.html', name="Jimmy") #in () file dirctory

app.run(debug=True)
