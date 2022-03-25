from flask import jsonify, make_response, request, Blueprint
from presenter.hoas import get_hoas, add_hoa
import json

from utilities import findObject

hoas_views = Blueprint("hoas", __name__)

# Get all HOAS


@hoas_views.route('/get-all-hoas', methods=['GET'])
def get_all_hoas():
    hoas = get_hoas()
    res = []
    for hoa in hoas:
        res.append(hoa.__dict__)
    return make_response(jsonify({"data": res, "responseCode": 200, "msg": "HOAS fetch successfully!"}), 200)

# Add or Create New HOA


@hoas_views.route('/create-hoas', methods=['POST'])
def add_hoas_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if "name" not in data:
        return make_response(jsonify({"status": "bad request"}), 400)
    if "address" not in data:
        return make_response(jsonify({"status": "bad request"}), 400)

    hoa_name = data["name"]
    hoa_address = data["address"]

    add_hoa(hoa_name, hoa_address)
    return make_response(jsonify({"msg": "HOA created successfully", "responseCode": 201}), 201)


# Get HOA by ID


@hoas_views.route('/get-hoas', methods=['GET'])
def get_user_by_id():
    hoasID = request.args.get('hoasId')

    if(hoasID == None):
        return make_response(jsonify({"msg": "hoasID is required!"}), 400)

    hoas = get_hoas()
    r = []
    for hoa in hoas:
        r.append(hoa.__dict__)

    data = findObject(r, 'id', int(hoasID))

    if data != None:
        return make_response(jsonify({
            "mas": "HOA fetch successfully!",
            "responseCode": 200,
            "data": data
        }), 200)
    else:
        return make_response(jsonify({"msg": "HOA not found"}), 200)
