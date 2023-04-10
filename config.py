import os


class Config:
    POSTGRES_URL = f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@{os.environ.get('POSTGRES_HOST')}:{os.environ.get('POSTGRES_PORT')}/{os.environ.get('POSTGRES_DB')}"
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    APP_SECRET_KEY = os.environ.get('APP_SECRET_KEY')
