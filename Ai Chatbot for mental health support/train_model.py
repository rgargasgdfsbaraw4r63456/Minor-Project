# train_model.py
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import joblib  # To save the model

# Load the dataset
with open('intent_dataset.json', 'r') as f:
    data = json.load(f)

intents = data['intents']

# Create our training data lists
tags = []       # The label (e.g., 'greeting', 'feeling_bad')
patterns = []   # The text to learn from (e.g., 'hi', 'hello')

for intent in intents:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])

# Create a Machine Learning pipeline
# 1. TF-IDF Vectorizer: Turns words into numbers
# 2. LinearSVC: A classifier that learns which numbers belong to which intent
model = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2), stop_words='english')),
    ('clf', LinearSVC())
])

# Train the model!
model.fit(patterns, tags)

# Save the trained model to a file so we don't have to retrain every time
joblib.dump(model, 'intent_classifier.joblib')
print("Model trained and saved!")