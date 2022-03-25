import json
from models.user import User



def get_users():
    f = open("../data/users.json")
    data = json.load(f)
    return data


def add_user(user: User):
    f = open("../data/users.json")
    data = json.load(f)
    f.close()

    user_json = json.loads(json.dumps(user.__dict__))
    data.append(user_json)
    with open("../data/users.json", 'w') as f:
        json.dump(data, f)
