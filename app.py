from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

svm_model = pickle.load(open("model/svm_model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))
label_encoder = pickle.load(open("model/label_encoder.pkl", "rb"))

def get_recommendation(label):
    if label == "Poor":
        return "Needs immediate academic support. Attend remedial classes and practice daily."
    elif label == "Average":
        return "Performance is average. Focus on weak subjects and revise regularly."
    elif label == "Good":
        return "Good performance. Maintain consistency and aim for excellence."
    else:
        return "No data available."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    iat1 = float(data["iat1"])
    iat2 = float(data["iat2"])
    model_mark = float(data["model_mark"])
    prev_year = int(data["prev_year"])

    X = np.array([[iat1, iat2, model_mark, prev_year]])
    X_scaled = scaler.transform(X)

    pred_encoded = svm_model.predict(X_scaled)[0]
    prediction = label_encoder.inverse_transform([pred_encoded])[0]
    recommendation = get_recommendation(prediction)

    return jsonify({
        "prediction": prediction,
        "recommendation": recommendation
    })

if __name__ == "__main__":
    app.run()
