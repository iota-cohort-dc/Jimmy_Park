from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/results', methods=["POST"])
def create_result():
    print "Received info"
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    description = request.form['description']

   # redirects back to the '/' route
    return render_template('submit_info.html', name = name, location = location, language = language, description = description)

app.run(debug=True) # run our server
