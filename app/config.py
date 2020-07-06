import os

class Config:
    '''
    Configuration parent class
    '''

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}