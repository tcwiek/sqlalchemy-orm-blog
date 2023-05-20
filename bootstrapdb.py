# # from models import  Base, Author, Article, Hashtag
# # from faker import Faker
# #
# #
# # def generate_authors(count=50):
# #     fake = Faker()
# #     return [
# #         Author(
# #             first_name=fake.first_name(),
# #             last_name=fake.last_name(),
# #             user_name=fake.user_name(),
# #             email=fake.email(),
# #         )
# #         for _ in range(count)
# #     ]
# #
# #
# # def generate_articles(count=100):
# #     fake = Faker()
# #     return [
# #         Article(
# #             title=fake.sentence(),
# #             content=fake.text(),
# #             author_id=fake.random_int(min=1, max=50),
# #         )
# #         for _ in range(count)
# #     ]
# #
# #
# # def main():
# #     # Create database tables
# #     Base.metadata.create_all()
# #
# #
# # if __name__ == "__main__":
# #     main()
#
#
# from faker import Faker
#
# from models import Base, Author, Article, Hashtag
# from session import session
#
#
# def generate_authors(session, count=50):
#     fake = Faker()
#     session.add_all([
#         Author(
#             first_name=fake.first_name(),
#             last_name=fake.last_name(),
#             user_name=fake.user_name(),
#             email=fake.email(),
#         )
#         for _ in range(count)
#     ])
#     session.commit()
#
#
# def generate_articles(session, count=10):
#     fake = Faker()
#     for author in session.query(Author):
#         author.articles.extend([
#             Article(
#                 title=fake.sentence(),
#                 content=fake.text(),
#             )
#             for _ in range(count)
#         ])
#     session.commit()
#
#
# def generate_hashtags(session, count=10):
#     fake = Faker()
#     for article in session.query(Article):
#         article.hashtags.extend([
#             Hashtag(name=fake.word())
#             for _ in range(count)
#         ])
#     session.commit()
#
#
# def main():
#     print("Creating database tables...")
#
#     # Create database tables
#     Base.metadata.create_all()
#
#     print("Generating authors, articles and hashtags...")
#
#     # Generate authors
#     generate_authors(session)
#
#     # Generate articles
#     generate_articles(session)
#
#     # Generate hashtags
#     generate_hashtags(session)
#
#     print("Done!")
#
#
# if __name__ == "__main__":
#     main()

from faker import Faker
from sqlalchemy.exc import IntegrityError

from models import Base, Author, Article, Hashtag
from session import session


def generate_authors(session, count=50):
    fake = Faker()
    session.add_all([
        Author(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            user_name=fake.user_name(),
            email=fake.email(),
        )
        for _ in range(count)
    ])
    session.commit()


def generate_articles(session, count=10):
    fake = Faker()
    for author in session.query(Author):
        author.articles.extend([
            Article(
                title=fake.sentence(),
                content=fake.text(),
            )
            for _ in range(count)
        ])
    session.commit()


def generate_hashtags(session, count=10):
    fake = Faker()
    for article in session.query(Article):
        hashtags = [
            Hashtag(name=fake.word())
            for _ in range(count)
        ]
        article.hashtags.extend(hashtags)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            continue


def main():
    print("Creating database tables...")

    # Create database tables
    Base.metadata.create_all()

    print("Generating authors...")

    # Generate authors
    generate_authors(session)

    print("Generating articles...")
    # Generate articles
    generate_articles(session)

    print("Generating hashtags...")
    # Generate hashtags
    generate_hashtags(session)

    print("Done!")


if __name__ == "__main__":
    main()