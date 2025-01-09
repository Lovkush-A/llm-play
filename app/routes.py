from flask import Blueprint, render_template, request, jsonify
from app.utils import get_pretrained_response, get_chatbot_response

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    text = data.get('text', '')
    
    pretrained_result = get_pretrained_response(text)
    chatbot_result = get_chatbot_response(text)
    
    return jsonify({
        'pretrained': pretrained_result,
        'chatbot': chatbot_result
    }) 