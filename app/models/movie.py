from typing import List
from models.actor import Actor

class Movie:
    def __init__(self, id, title, director, release_year, length_min, actors: List[Actor] = []):
        self.id = id
        self.title = title
        self.director = director
        self.release_year = release_year
        self.length_min = length_min
        self.actors = actors
