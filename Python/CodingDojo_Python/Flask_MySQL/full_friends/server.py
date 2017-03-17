from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "jimmy"
mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():

    query = "SELECT * FROM users" # running full_friends in database
    friends = mysql.query_db(query)
    return render_template("index.html", showfriends = friends, friends = friends)

@app.route("/friends", methods=["POST"])
def createFriend():



    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    mysql.query_db(query, data)

    return redirect("/")

@app.route("/friend/<user_id>/edit")
def edit(user_id):
    query = "SELECT * FROM users WHERE id = :user_id"
    data = {
    "user_id": user_id
    }
    single_friend = mysql.query_db(query, data)
    return render_template("/edit.html", friend=single_friend)


@app.route("/friends/<user_id>", methods=["POST"])
def update(user_id):
    query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, update_at = NOW() WHERE id = user_id"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "user_id": user_id
    }

    mysql.query_db(query, data)

    return redirect("/")

@app.route("/friends/<user_id>/delete", methods=["POST"])
def delete(user_id):
    query = "DELETE FROM users WHERE id = :user_id"
    data = {
        "user_id" : user_id
    }
    mysql.query_db(query,data)

    return redirect("/")

app.run(debug=True)
