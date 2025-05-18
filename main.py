from flask import Flask,render_template
from admin.blue import blue                        #since init is there we can import the files as modules in packages.
from logindir.login import login                   #since the blueprint is not in the same directory as main application we need to use the syntax from directoryname.modulename import object/var of blueprint
app = Flask(__name__)
#app.register_blueprint(blue,url_prefix="")       #first->the var of blueprint, when the blueprint is reg and the app runs it will first check the url_prefix whenever it gets a req.if it is null if it gets any matching route in blueprint it will be running even it is in the main .
app.register_blueprint(blue,url_prefix="/admin")  #the blueprint routes will work only if the url prefix matches url_prefix.
app.register_blueprint(login,url_prefix="/login")
@app.route("/")
def test():
    return "<h1>test</h1>"                      #if the blueprint is not reg or there is no same route it will be the homepage.

if __name__ =="__main__":
    app.run()


