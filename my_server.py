from flask import Flask
from flask_cors import CORS, cross_origin

# Khởi tạo Flask Server Backend
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

# Apply Flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Start Backend
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)