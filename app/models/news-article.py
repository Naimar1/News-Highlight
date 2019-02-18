class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,title,urlToImage,description,publishedAt,author):
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt
        self.author = author
       