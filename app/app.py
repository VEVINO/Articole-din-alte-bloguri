from flask import Flask, render_template, request, redirect, url_for
from blog import Blog
from article import Article

app = Flask(__name__)
my_blog = Blog()
# Exemplu de date pentru articole din alte bloguri (pentru demonstrație)
other_blog_articles = [
    {'title': 'Articolul 1 de invata Python usor si repede', 'url': 'https://www.itfactory.ro/all-courses/?gad_source=1&gclid'
                                                 '=Cj0KCQjw2PSvBhDjARIsAKc2cgO1kw8usjN10c9cZHP5si80a_C2roS994vptkeng4ggUU6fLqmI8nUaAkIfEALw_wcB'},
    {'title': 'Articolul 2 cu motivatia de a invata Python', 'url': 'https://teachbit.ro/blog/programare-python/'},
{'title': 'Articolul 3 din alt blog', 'url': 'https://blog2.com/articol3'},
    {'title': 'Articolul 4 din alt blog', 'url': 'https://blog2.com/articol4'},
    {'title': 'Articolul 5 din alt blog', 'url': 'https://blog3.com/articol5'},
    {'title': 'Articolul 6 din alt blog', 'url': 'https://blog3.com/articol6'}
]


@app.route('/')
def index():
    # Afișează articolele din alte bloguri în pagina HTML
    return render_template('index.html', other_blog_articles=other_blog_articles)


@app.route('/')
def home():
    return render_template('index.html', articles=my_blog.list_articles())


@app.route('/article/<title>')
def article_details(title):
    article = my_blog.get_article_by_title(title)
    if article:
        return render_template('article_details.html', article=article)
    else:
        return render_template('article_not_found.html', title=title)


@app.route('/create_article', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_article = Article(title, content)
        my_blog.add_article(new_article)
        return redirect(url_for('home'))
    return render_template('create_article.html')


# Adăugăm câteva articole pentru a avea date de afișat
article1 = Article("Articolul 1", "Conținutul articolului 1")
article2 = Article("Articolul 2", "Conținutul articolului 2")
my_blog.add_article(article1)
my_blog.add_article(article2)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
