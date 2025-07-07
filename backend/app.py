from flask import Flask, request, jsonify
import joblib
import numpy as np

# ✅ Step 1: Initialize Flask app
app = Flask(__name__)

# ✅ Step 2: Load ML model
model = joblib.load('risk_model.pkl')

# ✅ Step 3: Define route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    x = np.array([[data['mood'], data['sleep'], data['screen_time']]])
    prediction = model.predict(x)[0]
    levels = ['Low', 'Medium', 'High']
    return jsonify({'risk_level': levels[prediction]})

# ✅ Step 4: Run app
if __name__ == '__main__':
    app.run(debug=True)
