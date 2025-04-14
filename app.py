import streamlit as st
import joblib

# Load the saved model and vectorizer
model = joblib.load("pkl/spam_classifier_model.pkl")
vectorizer = joblib.load("pkl/tfidf_vectorizer.pkl")

# Apply background image using custom CSS
page_bg_img = '''
<style>
    .stApp {
        background-image: url("");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .title {
        font-family: 'Exo 2', sans-serif;
        font-style: italic;
        font-weight: bold;
        color: white;
        text-align: center;
        font-size: 36px;
        padding: 20px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
    }
</style>
'''
# Title
st.title("📩 SMS Spam Classifier")
st.write("This app uses a machine learning model to detect spam messages.")

# User input
user_input = st.text_area("Enter your message:")

# Predict button
if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Convert the input text to vector
        msg_vec = vectorizer.transform([user_input])
        prediction = model.predict(msg_vec)[0]
        result = "🚫 SPAM" if prediction == 1 else "✅ NOT SPAM"
        st.success(f"Prediction: {result}")
