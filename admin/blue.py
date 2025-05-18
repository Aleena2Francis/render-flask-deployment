from flask import Flask,Blueprint,render_template

blue = Blueprint("Blue",__name__,static_folder='static',template_folder='templates') #first parameter - name of the blueprint needed which flask uses internally. we use the var name for defining routes.__name__ tells Flask or Blueprint where this file is located.for more check chatgpt
                                                                           #static_folder and template_folder is necessary for divisional structure only as it needs diff temp and static for various blueprints
@blue.route("/")                                                           #https://explore-flask.readthedocs.io/en/latest/blueprints.html and https://flask.palletsprojects.com/en/stable/blueprints/
@blue.route("/home")
def home():
    return render_template("home.html")                                    #can't run a blueprint. just def it and import for use

@blue.route("/test")
def test():
    return "<h1>test</h1>"  


#for divisional structure we have moved the files needed for this application component into a separate folder/directory called admin.