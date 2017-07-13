from flask import Flask, render_template, request , redirect
app = Flask(__name__)

@app.route('/')
def survey():
  return render_template("index.html")

@app.route('/results',methods=['POST'])
def post_results():
    name = request.form['name']
    email = request.form['email']
    location = request.form['location']
    comments = request.form['comments']
    return render_template("results.html",name=name,email=email,location=location,comments=comments)



app.run(debug=True)
