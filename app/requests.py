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


def get_articles(category):
        '''
        Gets the json response to our url request
        '''
        get_articles_url = articles_url.format(api_key)
        print(get_articles_url)

        with urllib.request.urlopen(get_articles_url) as url:
                get_articles_data = url.read()
                get_articles_response = json.loads(get_articles_data)

                articles_results = None

                if get_articles_response['articles']:
                        articles_results_list = get_articles_response['articles']
                        articles_results = process_articles(articles_results_list)
        

        return articles_results
        


def process_articles(articles_list):
        '''
        Function  that processes the news result and transform them to a list of Objects
        Args:
            news_list: A list of sources that contain news details
        Returns :
            news_results: A list of news objects
        '''
        articles_results = []
        for articles_item in articles_list:
                id = articles_item['source']['id']
                name = articles_item['source']['name']
                author = articles_item['author']
                title = articles_item['title']
                description = articles_item['description']
                url= articles_item['url']
                urlToImage = articles_item['urlToImage']
                publishedAt = articles_item["publishedAt"]
                content = articles_item['content']
             

                articles_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt,content)
                articles_results.append(articles_object)

        return articles_results

def get_news(id):
        get_news_url = base_url.format(api_key)

        with urllib.request.urlopen(get_news_url) as url:
                get_news_data = url.read()
                get_news_response = json.loads(get_news_data)

                news_results = None

                
                if get_news_response['sources']:
                        news_results_list = get_news_response['sources']
                        news_results = process_news(news_results_list)
        return news_results

def process_news(news_list):
        '''
        Processes headlines results and returns a list of objects
        '''
        news_results = []
        for news_item in news_list:
                id = news_item['id']
                name = news_item['name']
                description = news_item['description']
                url = news_item['url']
                category = news_item['category']
                language = news_item['language']
                country = news_item['country']
                
                if name:
                    news_object = News(id,name,description,url,category,language,country)
                    news_results.append(news_object)	
            

            

        return news_results