from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name": 'My Wonderful Store',
        "items": [
            {
                "name": 'Emulsifier',
                "price": 15.99
            }
        ]
    }
]

# POST /store data={name: }
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    name = request_data["name"]
    store = { "name": name, "items": [] }
    return jsonify(store)

# GET /store
@app.route('/store', methods=['GET'])
def view_stores():
    return jsonify({ "stores": stores })

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def view_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    else:
        return jsonify({"message": "store not found"})

# POST /store/<string:name>/item data={name: , price: }
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    request_data = request.get_json()
    item_name = request_data["item_name"]
    item_price = request_data["item_price"]
    newItem = { "name": item_name, "price": item_price }
    
    for store in stores:
        if store["name"] == name:
            store["items"].append(newItem)
            return jsonify({"item": newItem})

    return jsonify({"message": "store with that name not found"})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def view_items(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["items"])

app.run(port=5000)