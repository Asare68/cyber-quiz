from flask import Flask, jsonify
from flask_cors import CORS  # To allow React Native to connect
import json

app = Flask(__name__)
CORS(app)  # Important: allows frontend to access API

# Load questions from JSON file
with open('/questions.json', 'r', encoding='utf-8') as f:
    quiz_data = json.load(f)

@app.route('/api/quiz', methods=['GET'])
def get_quiz():
    return jsonify(quiz_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)