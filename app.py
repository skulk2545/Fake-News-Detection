from scraper import fetch_article
from predictor import predict_news

if __name__ == "__main__":
    url = input("Enter a news article URL: ")
    try:
        title, content = fetch_article(url)
        print(f"\nTitle: {title}\n")
        result = predict_news(content)
        print(f"🧠 This news is predicted to be: **{result}**")
    except Exception as e:
        print(f"Error fetching article: {e}")
