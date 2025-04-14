import streamlit as st
import joblib

# Load the saved model and vectorizer
model = joblib.load("pkl/spam_classifier_model.pkl")
vectorizer = joblib.load("pkl/tfidf_vectorizer.pkl")

# Apply background image using custom CSS
page_bg_img = '''
<style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/BKY1601/spamly/main/res/img/bg.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
# Title
st.markdown("<h1 style='text-align: center;'>Spamly 📩</h1>", unsafe_allow_html=True)
st.write("Spamly app uses a machine learning model to detect spam messages.")

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
