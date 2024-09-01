from flask import Flask, render_template, request, jsonify
from app import app
from app.chatbot import get_response  # Ensure you have this function

@app.route('/')
def index():
    return render_template('KoJay fitness, your one stop to healthy living.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')  # Get user message from JSON
    response = get_response(user_input)  # Get bot response
    return jsonify({'response': response})  # Send back as JSON
