from command_processor import cp
from database import db

if __name__ == "__main__":
    cp.main()
    db.conn.close()
    db.cur.close()
