from enum import Enum
from models.actor import Actor
from models.movie import Movie
from database import db
from helpers import *


class AddCommandSwitches(Enum):
    ADD_ACTOR = "-p"
    ADD_MOVIE = "-m"


class AddCommand:
    def __init__(self):
        pass
    
    def reset(self):
        pass

    def get_precedence(self, switch):
        return 1

    def add_actor(self):
        name = ""
        birth_year = ""

        while True:
            name = input("Name: ")
            if not db.actor_exists(name):
                break
            else:
                print(f"{name} exists in the database.")

        while True:
            birth_year = input("Birth year: ")
            if is_valid_year(birth_year):
                break
            else:
                print(f"{birth_year} is not valid year.")

        db.add_data(Tables.actors, Actor(
            id=None, name=name, birth_year=birth_year))

    def add_movie(self):
        title = ""
        length = ""
        director = ""
        release_year = ""
        actors = []

        while True:
            title = input("Title: ")

            while True:
                length = input("Length: ")
                if is_valid_time_format(length):
                    break
                else:
                    print("Bad input format (hh:mm), try again!")

            while True:
                director = input("Director: ")
                if db.actor_exists(director):
                    break
                else:
                    print(f'We could not find "{director}", try again!')

            while True:
                release_year = input("Released in: ")
                if is_valid_year(release_year):
                    break
                else:
                    print(f"{release_year} is not a valid year.")

            while True:
                actor_input = input("Starring: ")

                if actor_input.lower() == "exit":
                    break

                if db.actor_exists(actor_input):
                    actors.append(Actor(*db.get_actor(actor_input)))
                else:
                    print(f'We could not find "{actor_input}", try again!')

            break

        db.add_data(Tables.movies, Movie(id=None, title=title, director=director, release_year=release_year,
                                         length_min=time_format_to_minutes(length), actors=actors))
