from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
username = 'root'
password = 'root'
host = '127.0.0.1'
port = '3306'
database = 'classicmodels'
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)
Base = declarative_base()
SessionLocal = sessionmaker(engine)
if __name__ == '__main__':
    db = SessionLocal()
    print(db)
    print(db.query(text(' SELECT test.snake_name AS test_snake_name FROM test ')).all())
