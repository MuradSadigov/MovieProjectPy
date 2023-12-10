from enum import Enum
from database import db


class DeleteCommandSwitches(Enum):
    DELETE_ACTOR = "-p"


class DeleteCommand:
    def __init__(self):
        pass

    def get_precedence(self, switch):
        return 1

    def delete_actor(self, name):
        db.delete_actor(name)
