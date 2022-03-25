from flask import jsonify, make_response, request, Blueprint
from presenter.user import get_users, add_user
from utilities import findObject
import json


user_views = Blueprint("user", __name__)

# Get All Users


@user_views.route('/get-all-users', methods=['GET'])
def get_all_users():
    users = get_users()
    res = []
    for user in users:
        res.append(user.__dict__)
    return make_response(jsonify({"data": res, "responseCode": 200, "msg": "Users fetch successfully!"}), 200)

# Add or Create New User


@user_views.route('/create-user', methods=['POST'])
def add_user_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if "user_name" not in data:
        return make_response(jsonify({"status": "bad request"}), 400)

    user_name = data["user_name"]

    add_user(user_name)
    return make_response(jsonify({"msg": "User created successfully", "responseCode": 201}), 201)


# Get user By ID


@user_views.route('/get-user', methods=['GET'])
def get_user_by_id():
    userID = request.args.get('userId')

    if(userID == None):
        return make_response(jsonify({"msg": "userId is required!"}), 400)

    users = get_users()
    r = []
    for user in users:
        r.append(user.__dict__)

    data = findObject(r, 'id', int(userID))

    if data != None:
        return make_response(jsonify({
            "mas": "User fetch successfully!",
            "responseCode": 200,
            "data": data
        }), 200)
    else:
        return make_response(jsonify({"msg": "user not found"}), 200)
