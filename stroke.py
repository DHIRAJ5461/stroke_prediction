import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Load the saved model
loaded_model = pickle.load(open('stroke.sav', 'rb'))

# Function for making predictions
def predict_stroke(input_data):
    # Perform any necessary preprocessing on the input data
    # ...

    # Make a prediction using the loaded model
    prediction = loaded_model.predict(input_data)
    return prediction

def main():
    st.title("Stroke Prediction")
    
    # Collect input data from the user
    #gender = st.number_input("Gender", min_value=0, max_value=1)
    gender=st.selectbox("Gender",("Female","Male","Other"))

    age = st.number_input("Age", min_value=0, max_value=120)
    
    
    hypertension = st.number_input("Hypertension", min_value=0, max_value=1)
    
    
    heart_disease = st.number_input("Heart Disease", min_value=0, max_value=1)
    
    ever_married = st.selectbox("Ever Married",("No","Yes"))
    
    work_type = st.selectbox("Work Type",("Govt_job", 'Never_worked' 'Private', 'Self-employed' ,'children'))
    
    residence_type = st.selectbox("Residence Type",('Rural', 'Urban'))
    
    avg_glucose_level = st.number_input("Average Glucose Level")
    
    bmi = st.number_input("BMI")
    
    smoking_status = st.selectbox("Smoking Status", ('Unknown' ,'formerly smoked', 'never smoked' ,'smokes'))

    if st.button("Predict"):
        gender_encoder = LabelEncoder()
        gender= gender_encoder.fit_transform([gender])[0]
        
        ever_married_encoder = LabelEncoder()
        ever_married=ever_married_encoder.fit_transform([ever_married])[0]
            
        
        work_type_encoder = LabelEncoder()
        work_type= work_type_encoder.fit_transform([work_type])[0]
        
        residence_type_encoder = LabelEncoder()
        residence_type=residence_type_encoder.fit_transform([residence_type ])[0]
        smoking_status_type_encoder = LabelEncoder()
    smoking_status=smoking_status_type_encoder.fit_transform([smoking_status])[0]
    
    
    
    
    input_data = [[gender, age, hypertension,  heart_disease,ever_married, work_type, residence_type,avg_glucose_level, bmi, smoking_status]]
    
    
        # Make a prediction
    prediction = predict_stroke(input_data)
    if prediction==0:
        result="No Stroke"
    else:
        result="Stroke"
    st.write("Prediction:", result)
    st.markdown("<h6><marquee>Thank you for visiting us!</marquee></h6>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()