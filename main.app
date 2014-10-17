from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
	return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
"""
if __name__ == '__main__':
	app.run(host='10.0.0.4', debug=True)
"""
