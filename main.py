from flask import Flask, jsonify, request
from flask_restful import Api, Resource

restApp = Flask(__name__)

users = [
    {"pid": 101, "name": "abc"},
    {"pid": 102, "name": "abe"},
    {"pid": 103, "name": "abg"},
    {"pid": 104, "name": "abj"},
]


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
    user = {"pid": request.json["pid"], "name": request.json["name"]}

    if findUser(users, user["pid"]):
        return jsonify({"Erorr": "User already exists"})
    else:
        users.append(user)
        return jsonify(users)


@restApp.route("/users", methods=["PUT"])
def modifySingleUserData():
    user = {"pid": request.json["pid"], "name": request.json["name"]}

    if findUser(users, user["pid"]):
        deleteUser(users, user["pid"])
        users.append(user)
        return jsonify(users)
    else:
        return jsonify({"Erorr": "User does not exist!"})


@restApp.route("/users/<int:id>", methods=["DELETE"])
def deleteSingleUserData(id):
    if findUser(users, id):
        deleteUser(users, id)
        return jsonify(users)
    else:
        return jsonify({"Erorr": "User does not exist!"})


def findUser(userList, pid):
    for u in userList:
        print(u["pid"], type(pid), type(u["pid"]))
        if u["pid"] == int(pid):
            res = True
            break
        else:
            res = False
    return res


def deleteUser(userList, pid):
    for u in userList:
        print(u["pid"], type(pid), type(u["pid"]))
        if u["pid"] == int(pid):
            users.remove(u)
            res = True
            break
        else:
            res = False
    return res


# server boot up
if __name__ == "__main__":
    restApp.run(debug=True, port=7200)
