from flask import render_template,request,redirect,url_for
from . import main
from app.requests import get_news
from ..models import News
from app.requests import get_articles
from unicodedata import category


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

 
 # Getting popular top headlines
    articles= get_articles(category)
    # business_news = get_news("business")
    # entertainment_news = get_news('entertainment')
    # sports_news = get_news('sports')
    title = 'Get all the breaking and latest news Highlights'
    
    return render_template('index.html', title = title, news=articles)

@main.route('/news')
def news_articles():
    
    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    
    title = f'{id} All news Highlights'
   

    return render_template('news.html',title = title, list = news  )

