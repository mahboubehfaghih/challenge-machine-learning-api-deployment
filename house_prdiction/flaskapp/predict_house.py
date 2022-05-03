from flask import Flask, request, render_template
import sklearn.externals
import joblib
import pandas as pd
import numpy as np
import pickle


app = Flask(__name__)

Number_of_bedrooms = 0
Living_area = 0
Number_of_facades = 0
Surface_area_land = 0
predicted_price = 0

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":

        model = pickle.load(open(r'C:\Users\Mahboubeh\Documents\GitHub\content\00.projects\4.deployment\New folder1\flaskapp\mlmodel\house_price_prediction.pkl', 'rb'))

        Number_of_bedrooms = int(request.form.get("Number of bedrooms"))
        Living_area = int(request.form.get("Living area"))
        Number_of_facades = int(request.form.get("Number of facades"))
        Surface_area_land= float(request.form.get("Surface area land"))

        new_house = np.array(
            [int(request.form["Number of bedrooms"]),
            int(request.form["Living area"]),
            int(request.form["Number of facades"]),
            float(request.form["Surface area land"]) ]).reshape(1, -1)
        predicted_price = model.predict(new_house)
        
        
    else:
        predicted_price=0
    return render_template("website.html",predicted_price=predicted_price)
if __name__ == '__main__':
    app.run(port= 5000, debug=True)