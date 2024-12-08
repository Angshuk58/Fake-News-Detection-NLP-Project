# Fake-News-Detection-NLP-Project

## Overview
The Fake News Detection project is a machine learning-based application designed to classify news articles as real or fake. Leveraging Natural Language Processing (NLP) techniques, this project aims to combat the spread of misinformation by analyzing the text content of news articles and determining their credibility.

## Features
1. Text Preprocessing: Cleans and preprocesses the text data to remove noise and prepare it for analysis.
2. TF-IDF Vectorization: Converts text data into numerical features using Term Frequency-Inverse Document Frequency (TF-IDF) vectorization.
3. Machine Learning Model: Utilizes Logistic Regression to classify news articles as real or fake.
4. Streamlit Web App: Provides an interactive web interface for users to input news text and get real-time predictions.

## Installation
1. git clone: https://github.com/your_username/fake-news-detection.git
              cd fake-news-detection
2. pip install -r requirements.txt

## Usage
1. Ensure the model and vectorizer files (model.pkl and vectorizer.pkl) are in the project directory.
2. streamlit run app.py
3. Open the provided URL in your web browser to access the web app.

## Files
1. model.pkl: Trained machine learning model for fake news detection.
2. vectorizer.pkl: TF-IDF vectorizer used for converting text data into numerical features.
3. app.py: Streamlit application script.
4. requirements.txt: List of required packages for the project.
5. fake_news_detection.ipynb: Jupyter notebook containing the code for training the model and preprocessing the data.

## Live App
You can try the **Fake News Detection** app live by clicking the link below:
[Try the Fake News Detection App] (https://angshuk58-fake-news-detection-nlp-project-app-z7gblt.streamlit.app)

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
