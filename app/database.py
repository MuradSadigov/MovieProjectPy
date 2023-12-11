import os
import psycopg2
from typing import List, Union
from psycopg2 import IntegrityError, OperationalError
from dotenv import load_dotenv
from models.actor import Actor
from models.movie import Movie
from helpers import *

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

            self.create_table(table="actors")
            self.create_table(table="movies")
            self.create_table(table="participation")

            print("Successful connection!")
        except OperationalError as e:
            print(f"Error: Unable to connect to the database.\n{e}")

    def create_table(self, table):
        try:
            self.cur.execute(
                f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table}')")
            table_exists = self.cur.fetchone()[0]
            if not table_exists:
                self.cur.execute(read_file(table))
                self.conn.commit()
        except Exception as e:
            print(f"Error: {e}")
            self.conn.rollback()
            print("Transaction rolled back.")

    def get_all_data(self, table_name: Tables) -> List[Union[Actor, Movie]]:
        try:
            data = []
            if table_name == Tables.actors:
                self.cur.execute("SELECT id, name, birth_year FROM actors")
                rows = self.cur.fetchall()
                
                for row in rows:
                    actor = Actor(*row)
                    data.append(actor)
                    
            elif table_name == Tables.movies:
                self.cur.execute(
                    "SELECT id, title, director, release_year, length_min FROM movies")
                movie_rows = self.cur.fetchall()

                for row in movie_rows:
                    movie = Movie(*row)

                    self.cur.execute(
                        f"SELECT actor_id FROM participation WHERE movie_id = {movie.id}")

                    actor_ids = self.cur.fetchall()
                    actors = []
                    for id in actor_ids:
                        self.cur.execute(
                            "SELECT id, name, birth_year FROM actors WHERE id = %s", (id,))
                        actor_row = self.cur.fetchone()
                        actor = Actor(*actor_row)
                        actors.append(actor)

                    movie.actors = actors
                    data.append(movie)

            return data
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Rolling back changes.")
            self.conn.rollback()

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

                for actor in data.actors:
                    self.cur.execute(
                        "SELECT id FROM actors WHERE name = %s",
                        (actor.name,)
                    )
                    actor_id = self.cur.fetchone()[0]
                    actor_ids.append(actor_id)

                for id in actor_ids:
                    self.cur.execute(
                        "INSERT INTO participation (movie_id, actor_id) VALUES (%s, %s)",
                        (movie_id, id)
                    )

            self.conn.commit()
        except IntegrityError:
            print("Data already exists in the database.")
            self.conn.rollback()
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Rolling back changes.")
            self.conn.rollback()

    def delete_actor(self, name):
        if self.actor_exists(name):
            if not self.is_director(name):
                try:
                    self.cur.execute(
                        "SELECT id FROM actors WHERE name = %s", (name,))
                    actor_id = self.cur.fetchone()[0]

                    self.cur.execute(
                        "DELETE FROM participation WHERE actor_id = %s", (actor_id,))

                    self.cur.execute(
                        "DELETE FROM actors WHERE name = %s", (name,))
                    self.conn.commit()
                except Exception as e:
                    print(f"Error deleting actor: {e}")
                    self.conn.rollback()
            else:
                print("Directors can not be deleted.")
        else:
            print(f"{name} cannot be found in the database.")

    def is_director(self, name):
        try:
            self.cur.execute(
                "SELECT * FROM movies WHERE director = %s", (name,))
            result = self.cur.fetchall()
            if result:
                return True
            return False
        except Exception as e:
            print(f"Error checking is director or actor: {e}")

    def actor_exists(self, name):
        try:
            self.cur.execute(
                "SELECT EXISTS (SELECT * FROM actors WHERE name = %s)", (name,))
            result = self.cur.fetchone()[0]
            return bool(result)
        except Exception as e:
            print(f"Error checking actor existence: {e}")

    def get_actor(self, name):
        try:
            self.cur.execute(
                "SELECT id, name, birth_year FROM actors WHERE name = %s", (name,))
            result = self.cur.fetchone()
            return result
        except Exception as e:
            print(f"Error getting actor from database: {e}")


db = Database()
