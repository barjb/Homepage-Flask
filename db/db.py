from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values

config = dotenv_values('.env')
POSTGRES_URL = f"postgresql://{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}@postgres-db:5432/{config['POSTGRES_DB']}"

engine = create_engine(POSTGRES_URL)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import models from .models
    Base.metadata.create_all(bind=engine)
