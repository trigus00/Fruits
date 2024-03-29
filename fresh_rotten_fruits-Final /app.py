# import necessary libraries
# from flask import Flask, render_template, redirect
import model_test
# from .model_test import *
from flask import Flask, render_template, redirect, request
# from tensorflow.keras.preprocessing import image
from PIL import Image
from io import BytesIO
# from xgboost import XGBClassifier
# import pandas as pd
# import numpy as np
# import pickle
import base64
import re
# import cStringIO

# create instance of Flask app
app = Flask(__name__)

prediction_probs = []
prediction_message = ""
all_classes = []
# imgstring = ""
# imgstring = "\\static\\img\\banana.png"
imgstring = "\\static\\img\\fruit-banner.jpg"

# create route that renders index.html template
@app.route("/")
def home():
    global prediction_probs, prediction_message, imgstring, all_classes
    return render_template("index.html", my_results = results, imgstring = imgstring, prediction_message = prediction_message, prediction_probs = prediction_probs, all_classes = all_classes)


@app.route("/results", methods=["GET", "POST"])
def results():

    global prediction_probs, prediction_message, imgstring, all_classes

    output_message = ""

    if request.method == "POST": 
        imgstring = request.form["imgtext"]
        imgdata = base64.b64decode(re.sub('^data:image/.+;base64,', '', imgstring))
        image = Image.open(BytesIO(imgdata)).convert('RGB')

        my_results, my_class_dict = model_test.results(image)
        # my_results, my_class_dict = model_test.results(imgdata)
        # my_results, my_class_dict = model_test.results(x)
        # my_class_dict = model_test.results()[2]
        # my_results_prob = my_results[1]
        prediction_probs = my_results[1][0]
        # all_classes = my_class_dict.items()
        all_classes = my_class_dict
        for key, value in my_class_dict.items():
            if value == my_results[0].item():
                # print('Prediction Class:',key)
                my_results_name = key

        prediction_message = my_results_name

    #return redirect("/", code=302)
    return redirect('validate')+'#team'


# @app.route("/", methods=["GET", "POST"])
# def home():
#     output_message = ""

#     if request.method == "POST":
#         imgstring = request.form["imgtext"]
#         imgstring = re.sub('^data:image/.+;base64,', '', imgstring)
#         imgdata = base64.b64decode(imgstring)
# scipy.misc.imresize(image, (224, 224, 3))

if __name__ == "__main__":
    app.run()
