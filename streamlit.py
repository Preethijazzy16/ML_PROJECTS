import streamlit as st
import requests

st.title('Insurance Premium Prediction')

# Split input fields into two columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Age', min_value=1, max_value=100, value=30)
    diabetes = st.selectbox('Diabetes', ['No', 'Yes'])
    blood_pressure_problems = st.selectbox('Blood Pressure Problems', ['No', 'Yes'])
    any_transplants = st.selectbox('Any Transplants', ['No', 'Yes'])
    any_chronic_diseases = st.selectbox('Any Chronic Diseases', ['No', 'Yes'])

with col2:
    height = st.number_input('Height (cm)', min_value=100, max_value=250, value=170)
    weight = st.number_input('Weight (kg)', min_value=30, max_value=200, value=70)
    known_allergies = st.selectbox('Known Allergies', ['No', 'Yes'])
    history_of_cancer_in_family = st.selectbox('History of Cancer in Family', ['No', 'Yes'])
    number_of_major_surgeries = st.number_input('Number of Major Surgeries', min_value=0, max_value=10, value=0)

    bmi = weight / ((height / 100) ** 2)
    has_major_health_issues = int(diabetes == 'Yes' or blood_pressure_problems == 'Yes' or any_chronic_diseases == 'Yes' or history_of_cancer_in_family == 'Yes')

# Create input data dictionary with feature name adjustments and Yes/No conversion
input_data = {
    'Age': age,
    'Diabetes': 1 if diabetes == 'Yes' else 0,
    'BloodPressureProblems': 1 if blood_pressure_problems == 'Yes' else 0,
    'AnyTransplants': 1 if any_transplants == 'Yes' else 0,
    'AnyChronicDiseases': 1 if any_chronic_diseases == 'Yes' else 0,
    'Height': height,
    'Weight': weight,
    'KnownAllergies': 1 if known_allergies == 'Yes' else 0,
    'HistoryOfCancerInFamily': 1 if history_of_cancer_in_family == 'Yes' else 0,
    'NumberOfMajorSurgeries': number_of_major_surgeries,
    'BMI': bmi,
    'HasMajorHealthIssues': has_major_health_issues
}

if st.button('Predict'):
    # Send request to Flask API
    response = requests.post('http://localhost:5000/predict', json=input_data)
    if response.status_code == 200:
        prediction = response.json()['premium']
        st.success(f'Predicted Premium: {prediction:.2f}')
    else:
        st.error('Error making prediction.')