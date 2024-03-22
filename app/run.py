# from blog import Blog
# from app.app import my_blog
from article import Article

from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

    # # Adăugare articole în blog
    # article1 = Article("Articolul 1", "Continutul articolului 1")
    # article2 = Article("Articolul 2", "Continutul articolului 2")
    # my_blog.add_article(article1)
    # my_blog.add_article(article2)
    #
    # # Afișare titluri articole
    # print("Titluri articole:")
    # for title in my_blog.list_articles():
    #     print(title)
    #
    # # Vizualizare detalii articol
    # article_title = "Articolul 1"
    # article = my_blog.get_article_by_title(article_title)
    # if article:
    #     print(f"\nDetalii articol '{article_title}':")
    #     print(f"Titlu: {article.get_title()}")
    #     print(f"Conținut: {article.get_content()}")
    # else:
    #     print(f"\nArticolul '{article_title}' nu a fost găsit.")