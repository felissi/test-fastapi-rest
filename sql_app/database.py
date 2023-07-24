from sqlalchemy import create_engine,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine(
    "mysql+pymysql://root:root@127.0.0.1:3306/classicmodels"
)
Base = declarative_base()
SessionLocal = sessionmaker(engine)
if __name__ == '__main__':
    db = SessionLocal()
    print(db)
    print(db.query(text(' SELECT test.snake_name AS test_snake_name FROM test ')).all())