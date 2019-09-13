import os

class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_KEY = '2fba2e985b9b466cbf2776e5dcfa728c'
    SECRET_KEY = 'MWIZA'

    NEWS_SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'

    NEWS_ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'productions':ProdConfig
}