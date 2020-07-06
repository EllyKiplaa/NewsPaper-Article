from app import app
import urllib.request,json
from .models import News,Articles

# News = news.News

#getting api key
apiKey = None


# getting the news url
base_url = None
articles_url = None

def configure_request(app):
        global apiKey,base_url,articles_url
        api_key = app.config['NEWS_API_KEY']
        base_url = app.config["NEWS_API_BASE_URL"]
        articles_url = app.config['ARTICLES_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of sources that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url= news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')
        language = news_item.get("language")

        news_object = News(id,name,description,url,category,country,language)
        news_results.append(news_object)

    return news_results

def get_articles(id):
    get_articles_url = base_url.format(id,apiKey)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if articles_results['articles']:
	        articles_articles = process_articles(articles_results['articles'])

	return articles_results

def process_articles(articles_list):
    	'''
	'''
	articles_results = []
	for article_item in articles_list:
		id = article_item.get('id')
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		urlToImage = article_item.get('urlToImage')
		publishedAt = article_item.get('publishedAt')
		
		if urlToImage:
			articles_object = Articles(id,author,title,description,url,urlToImage,publishedAt)
			articles_results.append(articles_object)	
		

		

		

	return articles_object