class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,overview,url,category,language,country):
        self.id =id
        self.name = name
        self.overview = overview
        self.url = url
        self.category = category
        self.language = language
        self.country = country

class Articles:
    '''
        Articles class to define articles objects
    '''
    def __init__(self,id,author,title,description,url,UrlToImage,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.UrlToImage = UrlToImage
        self.date = date
