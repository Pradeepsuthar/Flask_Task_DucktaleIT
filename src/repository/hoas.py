import json
from models.hoa import HOA


def get_hoas():
    f = open("../data/hoas.json")
    data = json.load(f)
    return data


def add_hoas(hoa: HOA):
    f = open("../data/hoas.json")
    data = json.load(f)
    f.close()

    hoa_json = json.loads(json.dumps(hoa.__dict__))
    data.append(hoa_json)
    with open("../data/hoas.json", 'w') as f:
        json.dump(data, f)
