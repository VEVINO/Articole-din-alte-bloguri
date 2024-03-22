from article import Article


class Blog:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def list_articles(self):
        return [article.get_title() for article in self.articles]

    def get_article_by_title(self, title):
        for article in self.articles:
            if article.get_title() == title:
                return article
        return None


class Article:
    pass
