from flask import Flask,render_template,Blueprint

login = Blueprint("login",__name__,static_folder='static',template_folder='templates')

@login.route("/",methods=["GET","POST"])
def log():
    return render_template("login.html")

