import logging
from flask import Flask, request, redirect, render_template, jsonify, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

logging.basicConfig(filename='./flaskapp/access.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p CST')

@app.route('/', methods=['GET'])
def home():
    app.logger.info('Request to \'/\' was made')

    return render_template('index.html')

@app.route('/api-docs')
def get_api_docs():
    app.logger.info('Redirecting to Redocly documentation')
    
    return redirect('http://192.168.1.78:65200', code=302)

@app.route('/users/<int:userId>', methods=['GET'])
def get_user(userId):
    app.logger.info(f'Request to \'/users/{userId}\' was made')
    
    # Placeholder for actual user fetching logic
    # In a real application, you would fetch the user from a database or another data source
    user = {
        "id": userId,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    if userId == 1:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)