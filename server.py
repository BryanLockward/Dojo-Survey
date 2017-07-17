from flask import Flask, render_template, request , redirect, flash
app = Flask(__name__)
app.secret_key="key"

@app.route('/')
def survey():
  return render_template("index.html")

@app.route('/results',methods=['POST'])
def post_results():

    name = request.form['name']
    if len(name)<1:
        flash("Error, NAME cannot be blank!")
        return redirect("/")

    email = request.form['email']
    if len(email)<1:
        flash("Error, Email cannot be blank!")
        return redirect("/")

    location = request.form['location']
    if len(location)<1:
        flash("Error, Location cannot be blank!")
        return redirect("/")

    comments = request.form['comments']
    if len(comments)>120:
        flash("Error, Comments cannot be more than 120 characters!")
        return redirect("/")

    elif len(comments)<1:
        flash("Error, Comments cannot be blank!")
        return redirect("/")

    return render_template("results.html",name=name,email=email,location=location,comments=comments)



app.run(debug=True)
