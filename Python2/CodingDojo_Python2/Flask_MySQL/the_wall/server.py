from flask import Flask,redirect, render_template,session, flash, request
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt
import bcrypt

app = Flask(__name__)
mysql = MySQLConnector(app, 'the_wall')
app.secret_key = "jimmy"
bcrypt = Bcrypt(app)

onlyLetters = re.compile(r'^[a-zA-Z]+$')
email_validation = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
    return render_template("login_registration.html")

@app.route("/reg_process", methods=["POST"])
def reg_process():
    flag = False
    data = {
        'first': request.form['first_name'],
        'last': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'cpassword': request.form['cpassword'],
    }
    if not onlyLetters.match(data['first']):
        flag = True
        flash('You can only have letters in your first name!')
    if len(data['first']) < 2:
        flag = True
        flash('Your First Name must be at least 2 characters!')
    if not data['first']:
        flag = True
        flash('You must submit a First Name!')
    if not onlyLetters.match(data['last']):
        flag = True
        flash('You can only have letters in your Last Name!')
    if len(data['last']) < 2:
        flag = True
        flash('Your Last Name must have at least 2 characters!')
    if not data['last']:
        flag = True
        flash('You must submit a Last Name!')

    if not email_validation.match(data['email']):
        flag = True
        flash('You must give a Valid Email!')
    if  not data['email']:
        flag = True
        flash('You must Enter an Email!')
    if len(data['password']) < 8:
        flag = True
        flash('Your Password must be at least 8 characters!')
    if not data['password']:
        flag = True
        flash('You must Enter a Password!')
    if data['password'] != data['cpassword']:
        flag = True
        flash('Your Passwords must match!')
    if flag:      # saying .. if flag is true: then...return /
        return redirect("/")
    else:
        pw_hash=bcrypt.generate_password_hash(data['password'])
        query = "INSERT INTO users(first_name,last_name,email,password,created_at,updated_at) VALUES(:first,:last,:email,:pass, NOW(),NOW())"
        query_data = {
            'first': data['first'],
            'last': data['last'],
            'email': data['email'],
            'pass': pw_hash,
        }
        user_id = mysql.query_db(query,query_data)
        # session['user_id'] = user_id
        flash("You are Registered. Please Login.")
        return redirect("/")

@app.route("/log_process", methods=["POST"])
def log_process():
    query = "SELECT * FROM users WHERE email = :email"
    data = {
        'email': request.form['email'],
    }
    userInQuestion = mysql.query_db(query,data)

    if not userInQuestion:
        flash('Invalid Email!')
    else:
        if bcrypt.check_password_hash(userInQuestion[0]['password'], request.form['password']):
            flash('Successful Login')
            session['user_id'] = userInQuestion[0]['id']
            session['logged_name'] = userInQuestion[0]['first_name']
            return redirect("/the_wall")
        else:
            flash('This Password is Invalid!')

    return redirect("/")

@app.route("/the_wall")
def the_wall():
    # if 'user_id' not in session:
    #     return redirect("/")

    query = "SELECT users.first_name, users.last_name, messages.messages, messages.created_at, messages.id FROM users JOIN messages ON users.id = messages.users_id ORDER BY messages.id DESC"

    # query2 = "SELECT users.first_name, users.last_name, comments.comments, comments.created_at, comments.id FROM messages JOIN comments ON messages.users_id = comments.users_id ORDER BY comments.id DESC"


    data = {
        "id": session['user_id']
    }
    result = mysql.query_db(query,data)
    # result2 = mysql.query_db(query2,data)
    # print result2
    # mysql.query_db(query,data)
    return render_template("the_wall.html", messages=result,name=session["logged_name"])

@app.route("/addMessage", methods=['POST'])
def addMessage():
    query = "INSERT INTO messages (messages, created_at, updated_at, users_id) VALUES (:message, NOW(), NOW(), :users_id)"
    data = {
        'message': request.form['messages'],
        'users_id': session['user_id'],
    }

    mysql.query_db(query,data)
    return redirect('/the_wall')

@app.route("/addMessage/<message_id>/addComment", methods=['POST'])
def addComment(message_id):
    print " query" * 58
    query = "INSERT INTO comments (messages_id, users_id, comment, created_at, updated_at) VALUES (:message_id, :users_id, :comment, NOW(),NOW())"

    data = {
        'message_id':message_id,
        'users_id': session['user_id'],
        'comment': request.form['comments'],
    }
    print "after after ~~~~~~" * 10
    print data
    mysql.query_db(query,data)
    return redirect("/the_wall")







@app.route("/logout")
def logout():
    session.clear()
    return render_template("login_registration.html")

app.run(debug=True)
