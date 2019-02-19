class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name):
        self.id = id
        self.name = name

class Article:
    '''Article class to define article objects'''

    def __init__(self,id,title,author,description,url,urlToImage,publishedAt):
        self.id = id
        self.title = title
        self.author= author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        
       