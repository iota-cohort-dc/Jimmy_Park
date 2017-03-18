from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

onlyLetters = re.compile(r'^[a-zA-Z]+$')
email_validation = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "jimmy"
mysql = MySQLConnector(app, 'the_wall')
bcrypt = Bcrypt(app) # this needs to go after app gets defined app ====

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def registerUser():
    flag = False
    data = {
    'email': request.form['email'],
    'first': request.form['first_name'],
    'last': request.form['last_name'],
    'password': request.form['password'],
    'cpassword': request.form['cpassword']
    }
    # First Name - letters only, at least 2 characters and that it was submitted
    if not onlyLetters.match(data['first']):
        flag = True
        flash('You can only have letters in your first name.')
    if len(data['first']) < 2:
        flag = True
        flash('Your first name must be at least 2 characters long.')
    if not data['first']:
        flag = True
        flash('You must submit a first name.')

    # Last Name - letters only, at least 2 characters and that it was submitted
    if not onlyLetters.match(data['last']):
        flag = True
        flash('You can only have letters in your last name.')
    if len(data['last']) < 2:
        flag = True
        flash('Your last name must be at least 2 characters long.')
    if not data['last']:
        flag = True
        flash('You must submit a last name.')

    # Email - Valid Email format, and that it was submitted
    if not email_validation.match(data['email']):
        flag = True
        flash('You must give a valid email.')
    if not data['email']:
        flag = True
        flash('You must enter an email.')

    # Password - at least 8 characters, and that it was submitted Password Confirmation - matches password
    if len(data['password']) < 8:
        flag = True
        flash('Your passord is too short.')
    if not data['password']:
        flag = True
        flash('You must submit a password')
    if data['password'] != data['cpassword']:
        flag = True
        flash("Your passwords don't match")

    if flag:
        return redirect("/")
    else:
        # send to DB
        pw_hash = bcrypt.generate_password_hash(data['password'])

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first, :last, :email, :pass, NOW(), NOW())"
        query_data = {
            "first": data['first'],
            "last": data['last'],
            "email": data['email'],
            "pass": pw_hash
        }

        user_id = mysql.query_db(query, query_data)
        session['user_id'] = user_id
        return redirect("/the_wall") # friendly redirect
#
@app.route("/login", methods=["POST"])
def login():
    query = "SELECT * FROM users WHERE  email = :email"
    data = {
        "email": request.form['email']
    }
    userInQuestion = mysql.query_db(query, data)

    if not userInQuestion:
        flash('Invalid Email.')
    else:
        if bcrypt.check_password_hash(userInQuestion[0]['password'], request.form['password']):
            session['user_id'] = userInQuestion[0]['id']
            return redirect("/the_wall")
        else:
            flash('This password is invalid.')

    return redirect ("/")

@app.route("/the_wall")
def the_wall():
    if 'user_id' not in session:
        return redirect("/")
    query = "SELECT * FROM users WHERE id = :id"
    data = {
        "id": session['user_id']
    }
    logged_user = mysql.query_db(query, data)

    q_messages = "SELECT users.first_name, users.last_name, messages.id AS message_id, messages.messages from messages LEFT JOIN users ON messages.users_id = users.id"
    messages = mysql.query_db(q_messages)

    c_messages = "SELECT users.first_name, users.last_name, comments.id AS comments_id, comments.comment, comments.messages_id FROM comments LEFT JOIN messages ON messages.user_id = users.id"
    comments = mysql.query_db(c_messages)

    # messages
    # comments
    return render_template("the_wall.html", user = logged_user[0], wall_messages = messages, wall_comments = comments)

@app.route("/addMessage", methods=["POST"])
def addMessage():
    query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(),NOW())"
    data = {
        "messsage": request.form['message'],
        "user_id": session['user_id'],
    }

    mysql.query_db(query, data)
    return redirect('/the_wall')

@app.route("/addComment", methods=["POST"])
def addComment():
    query = "INSERT INTO comments (message_id, user_id,comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())"
    data = {
        "message_id": request.form['message_id'],
        "user_id": session ['user_id'],
        "comment": request.form['comment']
    }

    mysql.query_db(query, data)
    return redirect("/the_wall")

@app.route("/logout")
def logout():
    session.clear()



app.run(debug=True)
