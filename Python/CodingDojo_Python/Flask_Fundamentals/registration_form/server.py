from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():


    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")

    if len(request.form['first_name']) < 1:
        flash('First name cannot be blank')
        print "test 1111111111111111111111111"
        return redirect('/')

    if len(request.form['last_name']) < 1:
        flash('Last name cannot be blank')
        print "test 2222222222222222222222222"
        return redirect('/')

    if len(request.form['password']) < 9:
        flash('Password has to be at least 8 characters')
        print "test 33333333333333333333333333"
        return redirect('/')

    if  request.form['confirm_pw'] != request.form['password']:
        flash('Password did not match')
        print "test 44444444444444444444444444"
        return redirect('/')

    else:
        print "Check this *******************"
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        confirm_pw = request.form['confirm_pw']
        print "test 5555555555555555555555555"

        return render_template('submit.html',email=email, first_name=first_name,last_name=last_name)

    # return redirect('/')


app.run(debug=True)
