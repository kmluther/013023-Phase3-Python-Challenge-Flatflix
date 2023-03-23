from .review import Review

class Movie:
    
    def __init__(self, title):    
        if type(title) == str and len(title) > 0:
            self._title = title
        self._reviews = []
        self._viewers = []

    def gettitle(self):
        return self._title

    def settitle(self, title):
        title

    title = property(gettitle, settitle)

    def getreviews(self):
        return self._reviews
    
    def setreviews(self, reviews):
        reviews

    reviews = property(getreviews, setreviews)

    def getreviewers(self):
        return self._viewers
    
    def setreviewers(self, viewers):
        viewers
    
    reviewers = property(getreviewers, setreviewers)

    def average_rating(self):
        total_rating = 0
        for review in self.reviews():
            total_rating += review.rating
        return total_rating / len(self.reviews())

    @classmethod
    def highest_rated(cls):
        pass
