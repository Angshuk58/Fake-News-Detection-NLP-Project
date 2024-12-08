import streamlit as st
import joblib

model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("Fake News Detection")
st.write("Enter the news text below to check if it's real or fake.")

user_input = st.text_area("Enter news text here")

if st.button("Predict"):
    if user_input:
        input_tfidf = vectorizer.transform([user_input])
        prediction = model.predict(input_tfidf)
        result = "Fake News" if prediction[0] else "Real News"
        st.write(f"The news is: **{result}**")
    else:
        st.write("Please enter some news text.")
