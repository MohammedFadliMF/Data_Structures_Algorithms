class Book:
    def __init__(self,id,title,author,pubYear):
        self.id=id
        self.title=title
        self.author=author
        self.pubYear=pubYear
    def __repr__(self):
        return "Book(id='{}' , title='{}' , author='{}' , pubYear='{}')".format(self.id,self.title,self.author,self.pubYear)
    def __str__(self):
        return self.__repr__()