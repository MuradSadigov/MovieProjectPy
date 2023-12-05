import os
import psycopg2
from typing import List, Union
from psycopg2 import IntegrityError, OperationalError
from dotenv import load_dotenv
from enum import Enum
from models.actor import Actor
from models.movie import Movie
from helpers import *


class Tables(Enum):
    movies = "movies"
    actors = "actors"
    participation = "participation"


class Database:
    conn = None
    cur = None

    def __init__(self):
        try:
            load_dotenv()

            self.conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
            self.cur = self.conn.cursor()

            self.create_table(table="movies")
            self.create_table(table="actors")
            self.create_table(table="participation")

            print("Successful connection!")
        except OperationalError as e:
            print(f"Error: Unable to connect to the database.\n{e}")

    def create_table(self, table: str):
        try:
            self.cur.execute(
                f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table}')")
            table_exists = self.cur.fetchone()[0]
            if not table_exists:
                self.cur.execute(read_file(table))
                self.conn.commit()
                print(f"Table '{table}' created successfully.")
            else:
                print(
                    f"Table '{table}' already exists. Skipped table creation.")
        except Exception as e:
            print(f"Error: {e}")
            self.conn.rollback()
            print("Transaction rolled back.")

    def add_data(self, table_name: Tables, data: Union[Movie, Actor]):
        try:
            if table_name == Tables.actors:
                self.cur.execute(
                    "INSERT INTO actors (name, birth_year) VALUES (%s, %s)",
                    (data.name, data.birth_year)
                )
            elif table_name == Tables.movies:
                actor_ids = []

                self.cur.execute(
                    "INSERT INTO movies (title, director, release_year, length_min) VALUES (%s, %s, %s, %s) RETURNING id",
                    (data.title, data.director, data.release_year, data.length_min)
                )
                movie_id = self.cur.fetchone()[0]

                self.cur.execute(
                    "SELECT id FROM actors WHERE name = %s", (data.director,))
                director_id = self.cur.fetchone()[0]

                for actor in data.actors:
                    self.cur.execute(
                        "SELECT id FROM actors WHERE name = %s",
                        (actor.name,)
                    )
                    actor_id = self.cur.fetchone()[0]
                    actor_ids.append(actor_id)

                for id in actor_ids:
                    is_director = True if id == director_id else False
                    self.cur.execute(
                        "INSERT INTO participation (movie_id, actor_id, is_director) VALUES (%s, %s, %s)",
                        (movie_id, id, is_director)
                    )

            self.conn.commit()
        except IntegrityError:
            print("Data already exists in the database.")
            self.conn.rollback()
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Rolling back changes.")
            self.conn.rollback()

    def update_data():
        pass

    def remove_data():
        pass

    def get_all_data(self, table_name: Tables) -> List[Union[Actor, Movie]]:
        data = []
        if table_name == Tables.actors:
            self.cur.execute("SELECT * FROM actors")
            rows = self.cur.fetchall()

            for row in rows:
                actor = Actor(*row)
                data.append(actor)

        return data

db = Database()
