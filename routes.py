from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/rsvp/', methods=['POST'])
def rsvp():
    print request
    name = request.form.get('name')
    return json.dumps({'status':'OK','name':name});


if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=True)
