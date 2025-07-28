from newspaper import Article

def fetch_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.title, article.text
