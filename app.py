import pickle
import flask
from flask import Flask, render_template, request
import numpy as np
#Load the file
with open("SPR.pkl", "rb") as f:
    model = pickle.load(f)
app = Flask(__name__)
@app.route("/")
def fun():
    return render_template("index.html")
@app.route("/predict",methods=["POST"])
def prediction():
    #creating the inputs
    hours_studied=int(request.form["Hours Studied"])
    previous_scores=int(request.form["Previous Scores"])
    extra_curricular_activities=int(request.form["Extracurricular Activities"]) #Yes:1 No:0
    sleep_hours=int(request.form["Sleep Hours"])
    sample_practice=int(request.form["Sample Question Papers Practiced"])
    features = np.array([[hours_studied,previous_scores,extra_curricular_activities,sleep_hours,sample_practice]])
    result = model.predict(features)[0]
    #Final result with 2 decimals
    final_result = f"{result:,.2f}"
    return render_template("index.html", prediction_text=final_result)
if __name__ == "__main__":
    app.run(debug=True)