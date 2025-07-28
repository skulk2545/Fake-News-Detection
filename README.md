# 📰 Fake News Detection System

This project detects whether a news article is REAL or FAKE using Natural Language Processing (NLP) and machine learning.

## 📁 Folder Structure

```
FakeNewsDetector/
├── app.py
├── scraper.py
├── predictor.py
├── model_training.py
├── nlp_preprocessing.py
├── news_model.pkl
├── vectorizer.pkl
├── fake_and_real_news_cleaned.csv
├── requirements.txt
└── __init__.py
```

## 🚀 Features

- Scrape live news articles using `newspaper3k`
- Preprocess text with NLP (cleaning, tokenizing, etc.)
- Train a `PassiveAggressiveClassifier` on real/fake news dataset
- Predict and classify articles as REAL or FAKE
- Export and reuse trained models

## 📦 Installation

```bash
git clone <your-repo-url>
cd FakeNewsDetector
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Linux/Mac

pip install -r requirements.txt
```

## 🛠️ Usage

### 1. Train the model (optional)
```bash
python model_training.py
```

### 2. Scrape and predict from a URL
```bash
python app.py
```

You can modify `app.py` to input your own article URLs.

## 🧠 Dataset

We use the combined dataset from:
- [Fake.csv](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- [True.csv](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

Merged and cleaned into: `fake_and_real_news_cleaned.csv`

## ✍️ Author

- Built by Shreya