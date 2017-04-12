from flask import Flask, render_template,redirect, flash, session, request
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friends_add_friends')

@app.route("/")
def index():

    query = mysql.query_db("SELECT * FROM friends")

    print "text"
    return render_template("index.html", postfriends=query)

@app.route("/process", methods=['POST'])
def process():

    print "~" * 30

    query = "INSERT INTO friends_add_friends.friends (name,age,friend_since,year,created_at,updated_at) VALUES (:name,:age,:friend_since,:year, NOW(), NOW())"

    print "+=" * 30

    data = {
             'name': request.form['name'],
             'age':  request.form['age'],
             'friend_since': request.form['frienddate'],
             'year': request.form['year']
           }
    mysql.query_db(query, data)

    print "<>" * 30
    return redirect("/")


app.run(debug=True)
