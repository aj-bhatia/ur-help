import os
from flask import Flask, render_template, abort, request, jsonify
from twilio.rest import Client
from replit import db

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

app = Flask(__name__)
IS_DEV = app.env == 'development'

@app.route('/', methods=['GET'])
def main():
    try:
        return render_template('index.html')
    except IndexError:
        abort(404)

@app.route('/add')
def create():
    """
        create() : Add document to Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        number = '+'+request.args.get('number')[1:]
        db[number]=True
        message = client.messages \
            .create(
                body='Thank you for joining URhelp! You will now receive updates about Red Alerts in Ukraine!',
                from_='+17194276351',
                to=number
                )
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection    """
    try:
        # Check for ID in URL query
        number = request.args.get('number')
        del db[number]
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/send')
def preSend():
    msg = request.args.get("location")
    link = request.args.get("link")
    return send(msg, link)
    
def send(msg, link):
    try:
      print(db.keys())
      for i in db:
        message = client.messages \
                .create(
                     body=msg+' If you would like to learn more: '+link,
                     from_='+17194276351',
                     to=i
                 )
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

port = int(os.environ.get('PORT', 5000)) 
def run():
    app.run(host='0.0.0.0',port=port, debug=True)
    
if __name__ == '__main__':
    run()