import os

class Config:
    '''
    Configuration parent class
    '''

    SOURCES_API_BASE_URL ='http://newsapi.org/v2/top-headlines?{}sources=bbc-news&{}api_key='
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&api_key={}'
    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}