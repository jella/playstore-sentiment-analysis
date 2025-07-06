from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)  # <---- habilita CORS

# Load trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'sentiment_model.pkl')
model = joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return "API is running. Use POST /predict"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' field in request."}), 400

    text = data['text']
    prediction = model.predict([text])[0]
    label = "Positive" if prediction == 1 else "Negative"

    return jsonify({"label": label})

if __name__ == "__main__":
    app.run(debug=True)
