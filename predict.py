import joblib
import pandas as pd
import numpy as np


# Load the trained model, scaler, and label encoder
model = joblib.load(r'animal_disease_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Function to make predictions based on user input
def predict_disease_from_input(animal_type,breed,age,gender,weight,symptom_1,symptom_2,symptom_3,symptom_4,duration,appetite_loss,vomiting,diarrhea,coughing,labored_breathing,lameness,skin_lesions,nasal_discharge,eye_discharge,body_temperature,heart_rate):
    # Prompt user for input data
    # animal_type = input("Enter Animal Type (e.g., Dog, Cat, Cow): ")
    # breed = input("Enter Breed (e.g., Labrador, Beagle, Siamese): ")
    # age = float(input("Enter Age: "))
    # gender = input("Enter Gender (Male/Female): ")
    # weight = float(input("Enter Weight (in kg): "))
    
    # # Symptoms (enter Yes/No)
    # symptom_1 = input("Symptom 1 (e.g., Fever, Coughing, Diarrhea, etc.): ")
    # symptom_2 = input("Symptom 2 (e.g., Lethargy, Sneezing, Vomiting, etc.): ")
    # symptom_3 = input("Symptom 3 (e.g., Appetite Loss, Nasal Discharge, etc.): ")
    # symptom_4 = input("Symptom 4 (e.g., Labored Breathing, Skin Lesions, etc.): ")
    
    # duration = input("Enter Duration of Symptoms (e.g., 1 week, 3 days): ")
    # appetite_loss = input("Appetite Loss (Yes/No): ")
    # vomiting = input("Vomiting (Yes/No): ")
    # diarrhea = input("Diarrhea (Yes/No): ")
    # coughing = input("Coughing (Yes/No): ")
    # labored_breathing = input("Labored Breathing (Yes/No): ")
    # lameness = input("Lameness (Yes/No): ")
    # skin_lesions = input("Skin Lesions (Yes/No): ")
    # nasal_discharge = input("Nasal Discharge (Yes/No): ")
    # eye_discharge = input("Eye Discharge (Yes/No): ")
    # body_temperature = float(input("Enter Body Temperature (in °C, e.g., 39.5): "))
    # heart_rate = int(input("Enter Heart Rate: "))

    # Create a DataFrame from the input data
    input_data = pd.DataFrame({
        'Animal_Type': [animal_type],
        'Breed': [breed],
        'Age': [age],
        'Gender': [gender],
        'Weight': [weight],
        'Symptom_1': [symptom_1],
        'Symptom_2': [symptom_2],
        'Symptom_3': [symptom_3],
        'Symptom_4': [symptom_4],
        'Duration': [duration],
        'Appetite_Loss': [appetite_loss],
        'Vomiting': [vomiting],
        'Diarrhea': [diarrhea],
        'Coughing': [coughing],
        'Labored_Breathing': [labored_breathing],
        'Lameness': [lameness],
        'Skin_Lesions': [skin_lesions],
        'Nasal_Discharge': [nasal_discharge],
        'Eye_Discharge': [eye_discharge],
        'Body_Temperature': [body_temperature],
        'Heart_Rate': [heart_rate]
    })

    # Handle unseen labels in categorical columns
    categorical_columns = [
        'Animal_Type', 'Breed', 'Gender', 'Symptom_1', 'Symptom_2', 
        'Symptom_3', 'Symptom_4', 'Duration', 'Appetite_Loss', 'Vomiting', 
        'Diarrhea', 'Coughing', 'Labored_Breathing', 'Lameness', 
        'Skin_Lesions', 'Nasal_Discharge', 'Eye_Discharge'
    ]

    for col in categorical_columns:
        if input_data[col][0] not in label_encoder.classes_:
            print(f"Warning: Unseen label '{input_data[col][0]}' in column '{col}'. Defaulting to a known value.")
            input_data[col] = label_encoder.transform([label_encoder.classes_[0]])  # Default to the first label
        else:
            input_data[col] = label_encoder.transform(input_data[col])
    
    # Scale continuous features (Age, Weight, Body_Temperature, Heart_Rate)
    try:
        input_data[['Age', 'Weight', 'Body_Temperature', 'Heart_Rate']] = scaler.transform(
            input_data[['Age', 'Weight', 'Body_Temperature', 'Heart_Rate']]
        )
    except Exception as e:
        print(f"Error during scaling: {e}")
        return

    # Make prediction for the input data
    try:
        prediction = model.predict(input_data)
        disease_prediction = label_encoder.inverse_transform(prediction)  # Decode the prediction
        print(f"Predicted Disease: {disease_prediction[0]}")
        return disease_prediction[0]
    except Exception as e:
        print(f"Error during prediction: {e}")

# # Example usage
# if __name__ == "__main__":
#     predict_disease_from_input()
