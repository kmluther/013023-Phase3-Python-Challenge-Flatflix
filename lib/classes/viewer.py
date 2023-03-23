from .review import Review

class Viewer:
    
    def __init__(self, username):
        if type(username) == str and 6 <= len(username) <= 16:
            self._username = username
        self._reviews = []
        self._movies = []

    def getusername(self):
        return self._username
    
    def setusername(self, username):
        self._username = username

    username = property(getusername, setusername)

    def getreviews(self):
        return self._reviews
    
    def setreviews(self, reviews):
        reviews

    reviews = property(getreviews, setreviews)

    def getreviewed_movies(self):
        return self._movies
    
    def setreviewed_movies(self, movies):
        movies
    
    reviewed_movies = property(getreviewed_movies, setreviewed_movies)

    def reviewed_movie(self, movie):
        return movie in self.reviewed_movies

    def rate_movie(self, movie, rating):
        pass