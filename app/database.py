import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv


class Database:
    conn = None

    def __init__(self):
        try:
            load_dotenv()

            conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
            
            self.create_table()
            
            print("Successful connection!")
        except OperationalError as e:
            print(f"Error: Unable to connect to the database.\n{e}")

    def create_table(schema_file_name: str):
        dirname = os.path.dirname(__file__)
        print(dirname)
        # try:
            
        #     with open("", "r") as file:
                
        #         pass
        # except e:
        #     print(e)
            