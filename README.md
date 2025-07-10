# 📩 Spamly – SMS Spam Classifier

**Spamly** is a machine learning-based SMS spam classifier built using **Python**, **Scikit-learn**, and **Streamlit**. It uses **Natural Language Processing (NLP)** techniques such as **TF-IDF vectorization** and **Multinomial Naive Bayes** to classify incoming messages as either **spam** or **ham** (not spam). The project offers an interactive web interface that allows users to test messages in real-time.

-------------

## Features

- Predicts whether an SMS message is **spam** or **ham**
- Trained on a real-world dataset of spam and ham messages
- Uses **TF-IDF** for text vectorization
- Deployed as a web app using **Streamlit**
- Simple UI for live input and prediction

------------

## Tech Stack

- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Streamlit  
- Pickle (for saving model and vectorizer)

## Project Structure
├── spam.csv # Dataset
├── spam_model.pkl # Trained spam classifier model
├── vectorizer.pkl # TF-IDF vectorizer
├── app.py # Streamlit web application
├── requirements.txt # List of dependencies
└── README.md # This file

---------------

## How to Run the Project

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/spamly.git
cd spamly

2. **Install dependencies**
pip install -r requirements.txt

3. **Run the Streamlit app**
streamlit run app.py

4. **Visit the app in your browser**
Default: http://localhost:8501

------------

📊 Sample Output
You enter:
"Congratulations! You've won a free iPhone. Click here to claim."

Spamly predicts:
Prediction: SPAM

📈 Future Enhancements
Add support for multiple languages

Track message history in session

Deploy online using platforms like Render or Hugging Face Spaces

-------------------

## 👨‍💻 Author

**Bipin Yadav**  
📧 bipinyadav919@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/bipin-yadav-jan16)  
🔗 [GitHub](https://github.com/BKY1601)
🔗 [Live project Link](https://spamly.streamlit.app/)


