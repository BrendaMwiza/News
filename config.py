import os

class Config:
    '''
    General config parent class
    '''

    NEWS_API_KEY = '2fba2e985b9b466cbf2776e5dcfa728c'
    SECRET_KEY = 'MWIZA'

    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/source?apiKey={}'

    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?source={}&apiKey={}'

class ProdConfig(Config):
    '''
    The production  config child class
    Args:
        Config: The parent config class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    The development  config child class
    Args:
        Config: The parent config class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'productions':ProdConfig
}