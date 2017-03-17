from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
from mysqlconnection import MySQLConnector
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'email')
app.secret_key = "jimmy"

@app.route('/', methods=['GET'])
def index():

    email = mysql.query_db("SELECT * FROM email") # running friends in database
    # print email
    return render_template("index.html",all_email = email)


@app.route('/submit', methods=['POST'])
def submit():
    errors = False

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        error = True

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        error = True

    if (errors == True):
        return redirect('/')
    else:
        session['email'] = request.form['email']
        query = "INSERT INTO email (email) VALUES (:email, NOW(), NOW())" #NOW(), NOW()
        data = {
             'email': request.form['email']
             }
        mysql.query_db(query, data)
        flash("The email address you entered() is a VALID email address!  Thank you!")
        return redirect('/')

    # We'll then create a dictionary of data from the POST data received.

app.run(debug=True)


    # if len(request.form['email']) < 1:
    #     flash("Email cannot be blank!")
    # elif not EMAIL_REGEX.match(request.form['email']):
    #     flash("Invalid Email Address!")
    #
    # else:
    #     email = request.form['email']
    #
    #     return render_template('/',email=email)
