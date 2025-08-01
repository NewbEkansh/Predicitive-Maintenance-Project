from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
import os

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# --- NOTE: The ML model is not used in this demo version ---
# In a real production environment, you would load the model here.
# try:
#     model = joblib.load('rul_model.pkl')
#     print("✅ Model loaded successfully!")
# except FileNotFoundError:
#     print("❌ Error: 'rul_model.pkl' not found.")
#     model = None

# --- API Route for Predictions ---
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()
    
    # --- REALISTIC SIMULATION HEURISTIC ---
    # This block simulates the model's behavior for the demo, as we can't
    # calculate the necessary historical features from a single input.
    # It creates a plausible RUL that responds to user input.
    try:
        # Start with a high base RUL
        base_rul = 220.0
        
        # Get key sensor values that indicate wear and tear from the input form
        # Default values are provided if a sensor is not in the input
        sensor_2 = data.get('sensor_2', 642.0)
        sensor_3 = data.get('sensor_3', 1580.0)
        sensor_4 = data.get('sensor_4', 1400.0)
        sensor_7 = data.get('sensor_7', 554.0)
        sensor_11 = data.get('sensor_11', 47.0)
        sensor_12 = data.get('sensor_12', 521.0)

        # Create a "wear score" based on how far the sensor values deviate from a healthy baseline.
        # The multipliers are tuned to give a reasonable response.
        s2_impact = max(0, (sensor_2 - 641.5) * 0.5)
        s3_impact = max(0, (sensor_3 - 1585.0) * 0.25)
        s4_impact = max(0, (sensor_4 - 1402.0) * 0.4)
        s7_impact = max(0, (sensor_7 - 553.0) * 0.6)
        s11_impact = max(0, (sensor_11 - 47.2) * 2.5)
        s12_impact = max(0, (sensor_12 - 521.0) * 0.7)
        
        # Sum the impact of each sensor's wear
        total_wear_score = s2_impact + s3_impact + s4_impact + s7_impact + s11_impact + s12_impact
        
        # Calculate the final predicted RUL
        predicted_rul = base_rul - total_wear_score
        
        # Ensure the RUL doesn't go below a realistic minimum
        predicted_rul = max(5.0, predicted_rul)
        
        # Return the simulated prediction as a JSON response
        return jsonify({'rul_prediction': round(predicted_rul, 2)})

    except Exception as e:
        # Return a JSON error message if anything goes wrong
        return jsonify({'error': f'An error occurred during simulation: {str(e)}'}), 400

# --- Route to serve the frontend ---
@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
