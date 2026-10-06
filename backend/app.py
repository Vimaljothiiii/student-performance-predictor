from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)

CORS(app)

with open("backend/model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return "Student Performance Predictor API is running!"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    values = [[
        data["study_hours"],
        data["attendance"],
        data["previous_score"],
        data["assignment_score"]
    ]]

    prediction = model.predict(values)[0]

    return jsonify({
        "prediction": prediction
    })


if __name__ == "__main__":
    app.run(debug=True)