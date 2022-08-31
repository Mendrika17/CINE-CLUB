import json

DATA_FILE = r"C:\Users\Mendrika\CINE-CLUB\data\movies.json"


class Movie:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def add_to_movies(self):
        movies_titles = Movie._get_movies()
        movies_titles.append(self.title)
        Movie._write_movies(movies_titles)
    
    def remove_from_movies(self):
        movies_titles = Movie._get_movies()
        movies_titles.remove(self.title)
        Movie._write_movies(movies_titles)

    @classmethod
    def _write_movies(cls, movies):
        with open(DATA_FILE, 'w') as json_file:
            json.dump(movies, json_file, indent=4)

    @classmethod
    def _get_movies(cls):
        with open(DATA_FILE, 'r') as json_file:
            return json.load(json_file)

    @classmethod
    def get_movies(cls):
        return [Movie(movie_title) for movie_title in Movie._get_movies()]