import pickle
from nlp_preprocessing import clean_text

# Load model and vectorizer
model = pickle.load(open("news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_news(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)
    return "REAL" if prediction[0] == 1 else "FAKE"
