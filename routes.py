import json
from flask import Flask, render_template, request

weddingapp = Flask(__name__)

@weddingapp.route('/')
def home():
	return render_template('index.html')

@weddingapp.route('/rsvp/', methods=['POST'])
def rsvp():
    print request
    name = request.form.get('name')
    return json.dumps({'status':'OK','name':name});


if __name__ == '__main__':
	weddingapp.run(host='127.0.0.1', debug=True)
