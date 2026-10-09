
from flask import Flask, request, jsonify
from chatbot import get_bot_response

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'response': 'Please enter a valid message.'}), 400

    bot_reply = get_bot_response(user_message)
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
  
