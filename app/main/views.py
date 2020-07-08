from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news
from ..models import News


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

 
 # Getting popular top headlines
    news_articles= get_news('')
    # business_news = get_news("business")
    # entertainment_news = get_news('entertainment')
    # sports_news = get_news('sports')
    title = 'Get all the breaking and latest news Highlights'
    
    return render_template('index.html', title = title, news=news_articles)

@main.route('/news/<int:id>')
def new_articles(id):
    
    '''
    View news page function that returns the news details page and its data
    '''
    articles = get_news(id)
    title = f'{id} All news Highlights'
   

    return render_template('headlines.html',title = title, news = articles )

