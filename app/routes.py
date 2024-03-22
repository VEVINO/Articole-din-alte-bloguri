from tokenize import Comment
from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app import db
from app.blog import Article

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')  # decorator pentru redirectionare HTTP
def index():
    # Afișează  articolele de pe prima pagină
    articles = Article.query.all()
    return render_template('index.html', articles=articles)


@app.route('/article/<int:article_id>')
def article(article_id):
    # Afișează un articol specific și comentariile sale
    article = Article.query.get_or_404(article_id)
    comments = Comment.query.filter_by(article_id=article.id).all()
    return render_template('article.html', article=article, comments=comments)


# @app.route('/author/<int:author_id>')
# def author(author_id):
#     # Afișează articolele scrise de un autor specific
#     author = Author.query.get_or_404(author_id)
#     articles = Article.query.filter_by(author_id=author.id).all()
#     return render_template('author.html', author=author, articles=articles)


@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    # Adaugă un nou articol în baza de date
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author_id = request.form['author_id']  # ne gandim că ID-ul autorului este trimis prin formular
        article = Article(title=title, content=content, author_id=author_id)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_article.html')
