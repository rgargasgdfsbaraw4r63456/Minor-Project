# app.py
from flask import Flask, render_template, request, jsonify
from responses import get_response

app = Flask(__name__)

@app.route('/')
def index():
    # This renders the HTML page
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # This is the API endpoint the frontend JavaScript will talk to
    user_message = request.json['message']
    bot_response = get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)