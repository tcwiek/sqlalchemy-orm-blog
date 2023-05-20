from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+pymysql://root:tomasz@localhost:3306/blog"
)
Session = sessionmaker(bind=engine)
session = Session()
