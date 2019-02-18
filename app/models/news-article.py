class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,poster,description,date):
        self.id =id
        self.title = title
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.description = description
        self.date = date
       