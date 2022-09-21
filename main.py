from flask import Flask, jsonify, request
from flask_restful import Api, Resource

restApp = Flask(__name__)

users = [{"pid": "abc"}, {"pid": "abd"}, {"pid": "abe"}, {"pid": "abf"}]


@restApp.route("/")
def helloWOrld():
    return "hello world!"


@restApp.route("/numbers/list/<int:num>", methods=["GET"])
def numberList(num):
    my_list = list(range(0, num, 1))
    print(my_list)
    return jsonify(my_list)


@restApp.route("/users", methods=["POST"])
def addSingleUserData():
    user = {"pid": request.json["pid"]}
    users.append(user)
    return jsonify(users)


# server boot up
if __name__ == "__main__":
    restApp.run(debug=True, port=7200)
