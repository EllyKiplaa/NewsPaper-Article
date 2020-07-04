from flask import render_template
from app import app

# Views
# Views
@app.route('/news/<int:news_id>')
def movie(news_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news.html',id = news_id)

def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title)