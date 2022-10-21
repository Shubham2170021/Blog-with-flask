from flask import Flask,render_template,request
app=Flask(__name__)
import requests
response=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data=response.json()
@app.route("/")
def home():
    return render_template ("index.html",data=data)
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/post")
def post():
    return render_template("post.html",data=data)
def contact():
    return render_template("contact.html")
def formentry():
    name=request.form["name"]
    email=request.form["email"]
    number=request.form["mobile"]
    message=request.form["message"]
    success="Successfully sent message"
    return render_template ("contact.html",success=success)
@app.route('/contact', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return formentry()
    else:
        return contact()
app.run(debug=True)