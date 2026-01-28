from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load quiz data from JSON file (OOP classes converted to dicts)
with open('questions.json', 'r', encoding='utf-8') as f:
    quiz_data = json.load(f)

@app.route('/api/quiz', methods=['GET'])
def get_quiz():
    return jsonify(quiz_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)