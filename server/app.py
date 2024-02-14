from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

# from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# migrate = Migrate(app, db)
# db.init_app(app)

api = Api(app)

class Home(Resource):

    def get(self):

        return make_response(
            {'Message': 'Hello'}
        )

api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(port=5555, debug=True)