import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
data = {}

api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("devices")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    return "Not Found"


class userList(Resource):
    def get(self):
        parser = reqparse.RequestParser()

        parser.add_argument('license', required=False)
        parser.add_argument('user', required=False)

        args = parser.parse_args()

        shelf = get_db()
        keys = list(shelf.keys())

        for key in keys:
            if shelf[key]['license'] == args['license']:
                return {
                    "license":shelf[key]['license'],
                    "user":shelf[key]['user']
                }
        return {'Status': 'Failure'}

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("auth", required =True)
        parser.add_argument('license', required=False)
        parser.add_argument('user', required=False)
        args = parser.parse_args()
        if args['auth'] == "vB3rsG3zhcEzHyf8gueXuYDTm7L0mIXE":
            shelf = get_db()
            shelf[args['license']] = args
            return {'Status': 'License key added', 'key': args['license']}, 201
        return {'Status':'Failed'}

    def delete(self):
        parser = reqparse.RequestParser()

        parser.add_argument('license', required=False)
        args = parser.parse_args()

        shelf = get_db()
        del shelf[args['license']]

        return {"License {0}".format(args['license']): 'Deleted'}



api.add_resource(userList, '/user_list')

if __name__ == '__main__':
    app.run(debug=True)


