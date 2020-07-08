import urllib.request,json
from .models import News,Articles

# News = news.News

#getting api key
api_key = None


# getting the news url
base_url = None
articles_url = None

def configure_request(app):
        global api_key,base_url,articles_url
        api_key = app.config['NEWS_API_KEY']
        base_url = app.config["NEWS_API_BASE_URL"]
        articles_url = app.config['NEWS_BASE_URL']


def get_news(category):
        '''
        Gets the json response to our url request
        '''
        get_news_url = articles_url.format(api_key)
        print(get_news_url)

        with urllib.request.urlopen(get_news_url) as url:
                get_news_data = url.read()
                get_news_response = json.loads(get_news_data)

                news_results = None

                if get_news_response['articles']:
                        news_results_list = get_news_response['articles']
                        news_results = process_articles(news_results_list)
        

        return news_results
        


def process_articles(news_list):
        '''
        Function  that processes the news result and transform them to a list of Objects
        Args:
            news_list: A list of sources that contain news details
        Returns :
            news_results: A list of news objects
        '''
        news_results = []
        for news_item in news_list:
                id = news_item['source']['id']
                name = news_item['source']['name']
                description = news_item['description']
                url= news_item['url']
                urlToImage = news_item['urlToImage']
                publishedAt = news_item["publishedAt"]
                content = news_item['content']
             

                news_object = News(id,name,description,url,urlToImage,publishedAt,content)
                news_results.append(news_object)

        return news_results

# def get_articles(id):
#         get_articles_url = base_url.format(id,api_key)

#         with urllib.request.urlopen(get_articles_url) as url:
#                 get_articles_data = url.read()
#                 get_articles_response = json.loads(get_articles_data)

#                 articles_results = None

#                 if articles_results['articles']:
#                     articles_articles = process_articles(articles_results['articles'])
#         return articles_results

# def process_articles(articles_list):
#         '''
#         Processes headlines results and returns a list of objects
#         '''
#         articles_results = []
#         for article_item in articles_list:
#                 id = article_item['id']
#                 author = article_item['name']
#                 title = article_item['title']
#                 description = article_item['description']
#                 url = article_item['url']
#                 urlToImage = article_item['urlToImage']
#                 publishedAt = article_item['publishedAt']
                
#                 if urlToImage:
#                     articles_object = Articles(id,author,title,description,url,urlToImage,publishedAt)
#                     articles_results.append(articles_object)	
            

            

#         return articles_object