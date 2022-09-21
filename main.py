from flask import Flask, jsonify
from flask_restful import Api, Resource

restApp = Flask(__name__)


@restApp.route("/")
def helloWOrld():
    return "hello world!"


@restApp.route("/numbers/list/<num>")
def numberList(num):
    my_list = list(range(0, int(num), 1))
    print(my_list)
    return jsonify(my_list)


# server boot up
if __name__ == "__main__":
    restApp.run(debug=True, port=7200)
