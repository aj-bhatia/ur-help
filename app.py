import os
from flask import Flask, render_template, abort, request, jsonify
from threading import Thread
from firebase_admin import credentials, firestore, initialize_app
from twilio.rest import Client

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACba081a875c23d6123891580da13da27c'
auth_token = '0d581ecedd0ec90098a4f71d8dbe7df5'
client = Client(account_sid, auth_token)

app = Flask(__name__)
IS_DEV = app.env == 'development'

@app.route('/', methods=['GET'])
@app.route('/index/')
def main():
    try:
        print(1)
        return render_template('index.html')
    except IndexError:
        abort(404)
    

@app.route('/project/')
def aboutProject():
    try:
        return render_template('index.html')
    except IndexError:
        abort(404)

@app.route('/aboutus/')
def aboutus():
    try:
        return render_template('index.html')
    except IndexError:
        abort(404)

@app.route('/join/')
def join():
    try:
        return render_template('index.html')
    except IndexError:
        abort(404)

@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        todo_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/list', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON
        todo : Return document that matches query ID
        all_todos : Return all documents    """
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('phoneNumbers')    
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/update', methods=['POST', 'PUT'])
def update():
    """
        update() : Update document in Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json['id']
        todo_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/send', methods=['POST', 'PUT'])
def send(msg):
    try:
        numbers = read()
        # for loop here with call to read() and put that val in the 'to' spot
        message = client.messages \
                .create(
                     body=str(msg[0]) + ' If you would like to learn more: ' + str(msg[1]),
                     from_='+17194276351',
                     to='+19493573519'
                 )
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

port = int(os.environ.get('PORT', 5000)) 
def run():
    app.run(host='0.0.0.0',port=port, debug=True)
    
if __name__ == '__main__':
    run()