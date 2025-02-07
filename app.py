from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained Linear Regression model
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Convert data to DataFrame for easier processing
    input_df = pd.DataFrame([data]) 
    prediction = model.predict(input_df)[0]
    return jsonify({'premium': prediction})

if __name__ == '__main__':
    app.run(debug=True)