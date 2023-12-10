from enum import Enum
from database import db
from helpers import *


class ListCommandSwitches(Enum):
    TITLE = "-t"
    DIRECTOR = "-d"
    ACTOR = "-a"
    ASCENDING = "-la"
    DESCENDING = "-ld"
    VIEW = "-v"

    @staticmethod
    def get_filtering_switches():
        return [ListCommandSwitches.TITLE.value, ListCommandSwitches.DIRECTOR.value,
                ListCommandSwitches.ACTOR.value, ListCommandSwitches.ASCENDING.value,
                ListCommandSwitches.DESCENDING.value]


class ListCommand:
    def __init__(self):
        self.actors = []
        self.movies = []
        self.reset()

    def reset(self):
        self.actors = db.get_all_data(Tables.actors)
        self.movies = db.get_all_data(Tables.movies)

    def get_precedence(self, switch):
        if switch == ListCommandSwitches.VIEW.value:
            return 2
        return 1

    def title(self, regex):
        pattern = re.compile(regex)
        self.movies = [
            movie for movie in self.movies if pattern.search(movie.title)]
        
    def director(self, regex):
        pattern = re.compile(regex)
        self.movies = [
            movie for movie in self.movies if pattern.search(movie.director)]
        
    def actor(self, regex):
        pattern = re.compile(regex)
        self.movies = [movie for movie in self.movies if any(pattern.search(actor.name) for actor in movie.actors)]

    def ascending(self):
        self.movies = sorted(self.movies, key=lambda movie: movie.length_min)

    def descending(self):
        self.movies = sorted(
            self.movies, key=lambda movie: movie.length_min, reverse=True)

    def list(self):
        for movie in self.movies:
            time_format = minutes_to_time_format(movie.length_min)
            print(f"""{movie.title} by {movie.director} in {
                movie.release_year}, {time_format}""")

    def view(self):
        for movie in self.movies:
            time_format = minutes_to_time_format(movie.length_min)
            print(f"""{movie.title} by {movie.director} in {
                movie.release_year}, {time_format}""")
            print("Starring:")
            for actor in movie.actors:
                print(f"""\t{actor.name} at age {
                    int(movie.release_year) - int(actor.birth_year)}""")
