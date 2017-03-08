from flask import Flask, render_template
app = Flask(__name__)

@app.route('/ninjas') #localhost:5000/success <--




def ninja_world(): #function name
    return render_template('index.html') #in () file dirctory

app.run(debug=True)
