# from session import session
# from models import Author, Article
#
#
# def main():
#     author = session.query(Author).get(1)
#     article = Article(
#         title="New article",
#         content="New article content"
#     )
#
#     author.articles.append(article)
#     session.commit()
#
#
# if __name__ == "__main__":
#     main()

from session import session
from models import Author, Article
from faker import Faker


def main():
    author = session.query(Author).get(6)
    fake = Faker()
    article = Article(
        title=fake.sentence(),
        content=fake.sentence(30)
    )

    author.articles.append(article)
    session.commit()


if __name__ == "__main__":
    main()
