from models.actor import Actor
from models.movie import Movie
from database import Tables, db
# from cli_handler import cli

if __name__ == "__main__":
    db.conn.close()
    db.cur.close()
