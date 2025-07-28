import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle

from nlp_preprocessing import clean_text

# Load dataset
df = pd.read_csv("C:\\Users\\anand\\Codes\\Neural Networks\\Fake News Detection\\fake_and_real_news.csv")
df['text'] = df['text'].fillna('')
df['label'] = df['label'].map({'FAKE': 0, 'REAL': 1})

# Clean text
df['cleaned'] = df['text'].apply(clean_text)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df['cleaned'], df['label'], test_size=0.2, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_df=0.7)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = PassiveAggressiveClassifier(max_iter=50)
model.fit(X_train_vec, y_train)

# Save model and vectorizer
pickle.dump(model, open("news_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
