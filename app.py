
import streamlit as st
import pickle
import numpy as np


@st.cache_resource
def load_model():
    with open("depression_model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

st.title("Teen Well-being Predictor")
st.image("https://i.pinimg.com/vwebp/1200x/95/50/7b/95507ba220ef508566c715ed9a6e13b1.webp", width=200)
st.header("Fill the given details to estimate your mental health:")



col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 10, 25, 16)
    daily_social_media_hours = st.number_input("Daily Social Media (Hours)", 0.0, 24.0, 3.0,step=0.1)
    sleep_hours = st.number_input("Sleep (Hours)", 0.0, 24.0, 7.0,step=0.1)
    screen_time_before_sleep = st.number_input("Screen Time Before Sleep (Hours)", 0.0, 10.0, 1.0,step=0.1)
    academic_performance = st.number_input("Academic Performance (0-5)", 0.0, 5.0, 3.0,step=0.1)
    physical_activity = st.number_input("Physical Activity (Hours)", 0.0, 10.0, 1.5,step=0.1)

with col2:
    stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)
    anxiety_level = st.slider("Anxiety Level (1-10)", 1, 10, 5)
    addiction_level = st.slider("Addiction Level (1-10)", 1, 10, 3)
    
    gender = st.selectbox("Gender", ["Male", "Female"])
    platform_usage = st.selectbox("Primary Platform", ["Instagram", "TikTok", "Both"])
    social_interaction_level = st.selectbox("Social Interaction Level", ["Low", "Medium", "High"])

gender_female = 1 if gender == "Female" else 0
gender_male = 1 if gender == "Male" else 0

platform_Both = 1 if platform_usage == "Both" else 0
platform_Instagram = 1 if platform_usage == "Instagram" else 0
platform_TikTok = 1 if platform_usage == "TikTok" else 0

social_high = 1 if social_interaction_level == "High" else 0
social_low = 1 if social_interaction_level == "Low" else 0
social_medium = 1 if social_interaction_level == "Medium" else 0

input_features = np.array([[
    age, daily_social_media_hours, sleep_hours, screen_time_before_sleep,
    academic_performance, physical_activity, stress_level, anxiety_level,
    addiction_level, gender_female, gender_male, platform_Both,
    platform_Instagram, platform_TikTok, social_high, social_low, social_medium
]])



# 4. Prediction Execution
if st.button("Run Prediction", type="primary", use_container_width=True):
    try:
        prediction = model.predict(input_features)[0]
        prediction_proba = model.predict_proba(input_features)[0]
        
        if prediction == 1:
            st.error(f"**Higher Risk Flagged** (Probability: {prediction_proba[1]*100:.2f}%)")
            st.image("https://i.pinimg.com/736x/eb/c8/9b/ebc89b36a6f9f09ce6fddf8c672fad1e.jpg",width=150)
        else:
            st.success(f"**Lower Risk / Normal** (Probability: {prediction_proba[0]*100:.2f}%)")
            st.image(f"https://i.pinimg.com/vwebp/1200x/4b/72/51/4b725167dcff98ee489e5dbbd69be923.webp",width=150)
            
    except Exception as e:
        st.error(f"Prediction failed: {e}")