import os

class Config:
    '''
    Configuration parent class
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'
    NEWS_BASE_URL = 'https://newsapi.org/v2/everything?q=language=en&from=2020-07-07&to=2020-07-07&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    @staticmethod
    def init_app(app):
        pass
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}