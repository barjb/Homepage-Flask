from dotenv import dotenv_values

config = dotenv_values('.env')


class Config:
    POSTGRES_URL = f"postgresql://{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}@{config['POSTGRES_HOST']}:{config['POSTGRES_PORT']}/{config['POSTGRES_DB']}"
