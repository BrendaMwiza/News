import os

class Config:
    '''
    General config parent class
    '''

    NEWS_API_KEY = '2fba2e985b9b466cbf2776e5dcfa728c'
    SECRET_KEY = 'MWIZA'

    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'

    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mwiza:umwiza1996@localhost/news'

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    The production  config child class
    Args:
        Config: The parent config class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    '''
    The development  config child class
    Args:
        Config: The parent config class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mwiza:password@localhost/News'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mwiza:umwiza1996@localhost/news_test'

    DEBUG = True

config_options = {
    'development':DevConfig,
    'productions':ProdConfig,
    'test':TestConfig
}