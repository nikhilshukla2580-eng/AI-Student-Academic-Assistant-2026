
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_chatbot_response, save_faq

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get('message', '')
    response = get_chatbot_response(user_msg)
    return jsonify({'response': response})

@app.route('/api/add-faq', methods=['POST'])
def add_faq():
    data = request.json
    category = data.get('category', 'General')
    question = data.get('question', '')
    answer = data.get('answer', '')
    
    if question and answer:
        save_faq(category, question, answer)
        return jsonify({'status': 'success', 'message': 'FAQ added successfully'})
    return jsonify({'status': 'error', 'message': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
