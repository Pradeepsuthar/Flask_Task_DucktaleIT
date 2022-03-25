from models.hoa import HOA
from typing import List
from repository import hoas


def get_hoas() -> List[HOA]:
    json_hoas = hoas.get_hoas()
    hoasd = []
    for json_hoa in json_hoas:
        h = HOA(json_hoa.get("id"), json_hoa.get(
            "name"), json_hoa.get("address"))
        hoasd.append(h)
    return hoasd


def add_hoa(name, address):
    hoas_id = len(hoas.get_hoas()) + 1
    new_hoas = HOA(hoas_id, name, address)
    hoas.add_hoas(new_hoas)
