import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')

@app.route('/add', method=['POST'])
def create():
    try:
        id = request.json['id']
        todo_ref.document(id).set(request.json)
        return jsonify({ "success": True }), 200
    except Exception as E:
        return f"An error occured {E}"

@app.route('/list', method=['GET'])
def read():
    try:
        #CHECK URL
        todo_id = request.args.get('id')
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            return jsonify(todo), 200
        else:
            all_todo = [doc.to_dict() for doc in todo_ref.stream()]
            return jsonify(all_todo), 200
    except Exception as e:
        return f"An error occurred {e}"

@app.route('/update', methods=['POST', 'PUT'])
def update():
    try:
        id = request.json[id]
        todo_ref.document(id).update(request.json)
        return jsonify({"Success": True}), 200
    except Exception as e:
        return f"An error occurred {e}"

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    try:
        #CHECK URL
        id = request.args.get(id)
        todo_ref.document(id).delete()
        return jsonify({"Success": True}), 200
    except Exception as e:
        return f"An error occurred {e}"

port = int(os.environ.get('PORT', 8080))

if name == __main__:
    app.run(threaded=True, host='0.0.0.0', port=port)