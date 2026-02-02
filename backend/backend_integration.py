"""
Flask Backend for AI Health Chatbot
Connects frontend chat UI with ML + NLP backend
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Allow imports from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chatbot.health_bot import HealthChatbot

app = Flask(__name__)
CORS(app)

# Initialize chatbot ONCE
chatbot = HealthChatbot(
    model_type="logistic",
    use_deep_learning=False
)

print("✅ AI Health Chatbot backend initialized")


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"error": "Message required"}), 400

        user_message = data["message"].strip()
        if not user_message:
            return jsonify({"error": "Empty message"}), 400

        # 🔥 MAIN INTEGRATION POINT
        response_text = generate_chat_response(user_message)

        return jsonify({
            "reply": response_text
        }), 200

    except Exception as e:
        print("❌ Backend error:", e)
        return jsonify({"error": "Internal server error"}), 500


def generate_chat_response(user_message):
    """
    Converts your ML + NLP output into chat-friendly text
    """

    # Step 1: Let chatbot process input
    result = chatbot.process_message(user_message)

    """
    result contains:
    - stress_level
    - confidence scores
    - disease risks
    - recommendations
    """

    # Step 2: Format response for frontend
    reply = f"""
🧠 **Stress Level:** {result['stress_level']}

📊 **Confidence**
• High: {result['confidence']['high']}%
• Medium: {result['confidence']['medium']}%
• Low: {result['confidence']['low']}%

⚠️ **High Risk Conditions**
"""

    for condition in result["high_risk_conditions"]:
        reply += f"• {condition}\n"

    reply += "\n💡 **Personalized Recommendations**\n"

    for tip in result["recommendations"]:
        reply += f"• {tip}\n"

    reply += """
⚠️ *Educational purpose only. Not medical advice.*
"""

    return reply


if __name__ == "__main__":
    print("\n🚀 Flask backend running on http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
