from flask import Flask
from flask import jsonify
from views.user import user_views
from views.hoas import hoas_views


app = Flask(__name__)

DEBUG_MODE = True
PORT = 5100
HOST = "0.0.0.0"

app.register_blueprint(user_views)
app.register_blueprint(hoas_views)

if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, host=HOST, port=PORT)
