from flask import Flask, render_template, request, redirect, flash
# import re
app = Flask(__name__)
app.secret_key = "jimmy"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def create_result():
    print "Received info"

    # name = request.form['name']
    # location = request.form['location']
    # language = request.form['language']
    # description = request.form['description']
    #
    # if len(request.form['name']) < 1:
    #     flash("Name cannot be empty")
    # else:
    #     flash("Success!")
    # if len(request.form['location']) < 1:
    #     flash("Location cannot be empty")
    # else:
    #     flash("Success!")
    # if len(request.form['language']) < 1:
    #     flash("Language cannot be empty") < 1
    # else:
    #     flash("Success!")

    if len(request.form['name']) < 1:
        flash('Name cannot be blank')
        return redirect('/')
        print "1111111111111111111111111"

    if len(request.form['description']) < 1:
        flash('No more than 120 characters')
        return redirect('/')
        print "2222222222222222222222222"
    else:
        print "Check!!!!!!!"
        name = request.form['name']
        place = request.form['place']
        language = request.form['language']
        comment = request.form['description']

        print "3333333333333333333333333"

        return render_template('submit_info.html',name=name, place=place,language=language,comment=comment)



   # redirects back to the '/' route
#     return render_template('submit_info.html', name = name, location = location, language = language, description = description)
#
app.run(debug=True) # run our server




    # return render_template('submitted.html',  name=name, place=place,language=language,comment=comment)
