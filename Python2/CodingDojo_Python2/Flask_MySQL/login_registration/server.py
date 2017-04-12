from flask import Flask, render_template,redirect, flash, session, request
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "jimmy"
mysql = MySQLConnector(app, 'login_registration')

onlyLetters = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['POST'])
def register():
    flag = False
    data = {
        'email': request.form['email'],
        'first': request.form['first_name'],
        'last': request.form['last_name'],
        'password': request.form['password'],
        'cpassword': request.form['cpassword'],
    }

    if not onlyLetters.match(data['first']):
        flag = True
        flash('You can only have letters in your First Name.')
    elif len(data['first']) < 2:
        flag = True
        flash('First name must have more than 2 characters.')
    elif not data['first']:
        flag = True
        flash('You must submit a first name.')
        # return redirect("/")

    elif not onlyLetters.match(data['last']):
        flag = True
        flash('You can only have letters in your Last Name')
    elif len(data['last']) < 2:
        flag = True
        flash('Last name must have more than  2 characters.')
    elif not data['last']:
        flag = True
        flash('You must submit a last name.')

    # elif not email
    #  left off hererererererererererererererererer

@app.route("/login", methods=['POST'])
def login():
    print "+=" * 30
    return redirect('/')

app.run(debug=True)
