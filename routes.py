import json
import datetime
from flask import Flask, render_template, request

weddingapp = Flask(__name__)

@weddingapp.route('/')
def home():
	return render_template('index.html')

@weddingapp.route('/rsvp', methods=['POST'])
def rsvp():
    print request
    print request.args
    name = request.form.get('name')
    email = request.form.get('email')
    people = request.form.get('people')
    event = request.form.get('event')


    filename = name.replace(" ", "_") + "---" + datetime.datetime.now().time().isoformat()
    with open(filename, 'w') as f:
        f.write(name + ", " + email + ", " + people + ", " + event + "\n")
    f.closed
    return json.dumps({'status':'OK','name':name});


if __name__ == '__main__':
	weddingapp.run(host='127.0.0.1', debug=True)
