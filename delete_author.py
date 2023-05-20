# from models import Author, Article
# from session import session
#
#
# def main():
#     author = Author.query(Author).get(6)
#     articles_count = len(author.articles)
#
#     assert author is not None
#     assert articles_count != 0
#
#     session.delete(author)
#     session.commit()
#
#     assert session.query(Author).get(7) is None
#     articles = session.query(Article).filter_by(author_id=author.id).all()
#     assert len(articles.all()) == 0
#
#
# if __name__ == "__main__":
#     main()

from models import Author, Article
from session import session


def main():
    author = session.query(Author).get(1)
    assert author is not None, "Author with id 7 not found"

    articles_count = len(author.articles)
    assert articles_count != 0, "Author has no articles"

    session.delete(author)
    session.commit()

    assert session.query(Author).get(7) is None, "Author not deleted"

    articles = session.query(Article).filter_by(
        author_id=author.id
    )
    assert len(articles.all()) == 0, "Author's articles not deleted"


if __name__ == "__main__":
    main()
