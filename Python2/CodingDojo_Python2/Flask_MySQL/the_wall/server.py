from flask import Flask
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "jimmy"
mysql = MySQLConnector(app, 'the_wall')

@app.route("/users")
def index():
    query = "SELECT * FROM user WHERE id = 1"
    users = mysql.query_db(query)

    print mysql.query_db("SELECT * FROM users")
    
    return render_template("index.html")

app.run(debug=True)
