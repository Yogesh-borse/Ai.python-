from flask import Flask

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return "<h1>Welcome to My Website</h1>"

# Route for the about page
@app.route('/about')
def about():
    return "<h1>yogesh_borse01</h1><p>This is a simple Flask app.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
