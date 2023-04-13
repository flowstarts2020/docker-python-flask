from flask import Flask
from jinja2.utils import markupsafe
app = Flask(__name__)

@app.route('/')
def response():
    return '<h1>Hello from Flask & Docker</h2>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
