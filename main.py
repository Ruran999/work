from flask import Flask
from flask import jsonify, request
from db.db import Database
from sqlite3 import connect

DATABASE_NAME = "product.db"

db = Database(connect(DATABASE_NAME, check_same_thread=False))

app = Flask(__name__)

@app.route('/products', methods=["GET"])
def get_product():
    product = db.get_products()
    return jsonify(product)

@app.route("/product", methods=["POST"])
def post_product():
    product_details = request.get_json()
    print(product_details)
    name = product_details["name"]
    price = product_details["price"]
    age = product_details["age"]
    weight = product_details["weight"]
    rating = product_details["rating"]
    result = db.insert_product(name, price, age, weight, rating)
    return jsonify(result)

@app.route("/product/<id>", methods=["GET"])
def product_by_id(id):
    product = db.get_product_by_id(id)
    return jsonify(product)

@app.route("/product/<id>", methods=["DELETE"])
def delete_product(id):
    result = db.del_product_by_id(id)
    return jsonify(result)

@app.route('/clients', methods=["GET"])
def get_all_clients():
    clients = db.get_clients()
    return jsonify(clients)

@app.route("/client", methods=["POST"])
def insert_one_client():
    client_details = request.get_json()
    print(client_details)
    name = client_details["name"]
    age = client_details["age"]
    result = db.insert_client(name, age)
    return jsonify(result)

@app.route("/client/<id>", methods=["GET"])
def get_one_client_by_id(id):
    client = db.get_client_by_id(id)
    if client[3] is not None:
        client_with_product = db.get_client_with_product(id)
        return jsonify(client_with_product)
    return jsonify(client)

@app.route("/client/<id>", methods=["DELETE"])
def delete_client(id):
    result = db.del_client_by_id(id)
    return jsonify(result)

@app.route("/client/<id>/product/<product_id>", methods=["PUT"])
def add_product_to_client_by_id(product_id, id):
    add_product_by_id = db.add_product_id_for_client(product_id, id)
    return jsonify(add_product_by_id)

if __name__ == "__main__":
    db.create_tables()
    app.run(host='0.0.0.0', port=8000, debug=False)