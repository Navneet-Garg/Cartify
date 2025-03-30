from flask import Blueprint, request, jsonify
from app.models.chatbot_model import get_gemini_response
from app.config.settings import ALLOWED_ORIGINS
from flask_cors import CORS

bp = Blueprint('chatbot', __name__)
CORS(bp, resources={r"/chat": {"origins": ALLOWED_ORIGINS}})

@bp.route("/chat", methods=["POST"])
def chat_endpoint():
    message = request.json.get("message")
    if message:
        response = get_gemini_response(message)
        return jsonify({"bot": response})
    else:
        return jsonify({"bot": "Please send a valid message."}) 