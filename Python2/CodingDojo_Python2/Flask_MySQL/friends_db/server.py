from flask import Flask,request,redirect,render_template,session,flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route("/")
def index():
    # print "*" * 8
    friends = mysql.query_db("SELECT * FROM friends")
    # print friends
    # print "=" * 8
    return render_template("index.html", postfriends=friends)

@app.route("/process", methods=["POST"])
def process():

    print "~" * 30

    query = "INSERT INTO friendsdb.friends (first_name,last_name,occupation,created_at,updated_at) VALUES (:first_name,:last_name,:occupation, NOW(), NOW())"
    print "+=" * 30

    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)

    print "<>" * 30
    return redirect("/")

app.run(debug=True)
