# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html", About = "About" ) 

# @app.route("/about")
# def about():

# @app.route("/test")
# def test():
    
# @app.route("/train")
# def train():

# @app.route("/validate")
# def validate():

# @app.route("/team")
# def team():



if __name__ == "__main__":
    app.run(debug= True )
