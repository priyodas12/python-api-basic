from flask import Flask
from flask_restful import Api, Resource

restApp = Flask(__name__)
restApi = Api(restApp)


class NumberList(Resource):
    def get(self):
        print("Server Up")
        return [1, 2, 3, 4]


# binding Class to endpoints
restApi.add_resource(NumberList, "/numbers")


# server boot up
if __name__ == "__main__":
    restApp.run(debug=True)
