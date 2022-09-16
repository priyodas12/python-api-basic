from flask import Flask
from flask_restful import Api, Resource

restApp = Flask(__name__)
restApi = Api(restApp)


class NumberList(Resource):
    def get(self):
        print("Server Up")
        return [1, 2, 3, 4]


class Persons(Resource):
    def get(self, name):
        return "Hello {}".format(name)


# binding Class to endpoints
restApi.add_resource(NumberList, "/numbers")
restApi.add_resource(Persons, "/persons/<string:name>")


# server boot up
if __name__ == "__main__":
    restApp.run(debug=True)
