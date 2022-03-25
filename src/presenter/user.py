from models.user import User
from typing import List
from repository import user


def get_users() -> List[User]:
    json_users = user.get_users()
    users = []
    for json_user in json_users:
        u = User(json_user.get("id"), json_user.get("username"))
        users.append(u)
    return users


def add_user(user_name):
    user_id = len(user.get_users()) + 1
    new_user = User(user_id, user_name)
    user.add_user(new_user)
