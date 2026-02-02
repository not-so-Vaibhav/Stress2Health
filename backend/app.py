from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import sys
import os
import warnings

# Suppress sklearn version mismatch and feature-name warnings (model works correctly)
warnings.filterwarnings("ignore", message="Trying to unpickle estimator")
warnings.filterwarnings("ignore", message="X does not have valid feature names")

# allow imports from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chatbot.health_bot import HealthChatbot

app = Flask(__name__)
CORS(app)

# initialize chatbot once
try:
    print("🔄 Initializing AI Health Chatbot...")
    chatbot = HealthChatbot(model_type="logistic", use_deep_learning=False)
    
    # Verify model is working by testing predict method
    print("🔍 Verifying model...")
    if hasattr(chatbot.stress_predictor, 'predict'):
        # Test prediction to ensure model works
        try:
            test_prediction = chatbot.stress_predictor.predict(
                sleep_hours=7.0,
                physical_activity='medium',
                work_hours=8.0,
                social_interaction='medium'
            )
            print(f"✅ Model verification successful! Test prediction: {test_prediction}")
        except Exception as test_error:
            print(f"⚠️  Model verification failed: {test_error}")
            print("   The model may still work, but there might be issues.")
    else:
        print("⚠️  Warning: predict method not found on stress_predictor")
    
    print("✅ Chatbot initialized successfully!")
except Exception as e:
    print(f"❌ Error initializing chatbot: {e}")
    import traceback
    traceback.print_exc()
    chatbot = None

# -----------------------------
# In-memory conversation store
# -----------------------------
sessions = {}

QUESTIONS = [
    ("text", "How are you feeling today? (Describe your stress, mood, or concerns)"),
    ("sleep_hours", "How many hours do you sleep on average per night?"),
    ("bmi", "What is your Body Mass Index (BMI)?"),
    ("physical_activity", "What is your physical activity level? (low / medium / high)"),
    ("work_hours", "How many hours do you work per day on average?"),
    ("social_interaction", "What is your social interaction level? (low / medium / high)")
]


@app.route("/")
def index():
    return jsonify({
        "app": "Stress2Health",
        "status": "ok",
        "message": "API is running. Use POST /chat to interact.",
        "health": "/health"
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/chat", methods=["POST"])
def chat():
    if chatbot is None:
        return jsonify({
            "error": "Chatbot not initialized. Please check backend logs."
        }), 503
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        user_message = data.get("message", "").strip()
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400
        
        session_id = data.get("session_id")

        # create new session
        if not session_id or session_id not in sessions:
            session_id = str(uuid.uuid4())
            sessions[session_id] = {
                "step": 0,
                "answers": {}
            }
            return jsonify({
                "reply": QUESTIONS[0][1],
                "session_id": session_id
            }), 200

        session = sessions[session_id]
        step = session["step"]

        if step >= len(QUESTIONS):
            return jsonify({
                "error": "Session already completed. Please start a new conversation."
            }), 400

        # Validate input based on question type
        key, question_text = QUESTIONS[step]
        
        # Validate numeric inputs
        if key in ["sleep_hours", "bmi", "work_hours"]:
            try:
                value = float(user_message)
                if key == "sleep_hours" and (value < 0 or value > 24):
                    return jsonify({
                        "error": "Please enter a valid number of sleep hours (0-24)"
                    }), 400
                elif key == "bmi" and (value < 10 or value > 50):
                    return jsonify({
                        "error": "Please enter a valid BMI (typically 10-50)"
                    }), 400
                elif key == "work_hours" and (value < 0 or value > 24):
                    return jsonify({
                        "error": "Please enter a valid number of work hours (0-24)"
                    }), 400
            except ValueError:
                return jsonify({
                    "error": f"Please enter a valid number for {key.replace('_', ' ')}"
                }), 400
        
        # Validate categorical inputs
        elif key in ["physical_activity", "social_interaction"]:
            value = user_message.lower().strip()
            if value not in ['low', 'medium', 'high']:
                return jsonify({
                    "error": f"Please enter 'low', 'medium', or 'high' for {key.replace('_', ' ')}"
                }), 400

        # save answer
        session["answers"][key] = user_message
        session["step"] += 1

        # ask next question
        if session["step"] < len(QUESTIONS):
            next_question = QUESTIONS[session["step"]][1]
            return jsonify({
                "reply": next_question,
                "session_id": session_id
            }), 200

        # ---------------------------------
        # ALL DATA COLLECTED → RUN ANALYSIS
        # ---------------------------------
        answers = session["answers"]

        # Validate and convert inputs
        try:
            sleep_hours = float(answers["sleep_hours"])
            bmi = float(answers["bmi"])
            work_hours = float(answers["work_hours"])
        except (ValueError, KeyError) as e:
            return jsonify({
                "error": f"Invalid input: {str(e)}. Please provide valid numbers."
            }), 400

        # Validate activity and social interaction
        physical_activity = answers["physical_activity"].lower().strip()
        social_interaction = answers["social_interaction"].lower().strip()
        
        if physical_activity not in ['low', 'medium', 'high']:
            return jsonify({
                "error": "Physical activity must be 'low', 'medium', or 'high'"
            }), 400
        
        if social_interaction not in ['low', 'medium', 'high']:
            return jsonify({
                "error": "Social interaction must be 'low', 'medium', or 'high'"
            }), 400

        # Predict stress level
        try:
            # Verify model is loaded
            if chatbot.stress_predictor.model is None:
                return jsonify({
                    "error": "Model not loaded. Please ensure models are trained and available."
                }), 500
            
            # Check if predict method exists
            if not hasattr(chatbot.stress_predictor, 'predict'):
                return jsonify({
                    "error": "Predict method not found. Model may not be initialized correctly."
                }), 500
            
            # Make prediction
            stress_level = chatbot.stress_predictor.predict(
                sleep_hours=sleep_hours,
                physical_activity=physical_activity,
                work_hours=work_hours,
                social_interaction=social_interaction
            )
            
            # Validate prediction result
            if stress_level is None:
                return jsonify({
                    "error": "Prediction returned None. Model may not be working correctly."
                }), 500
                
        except AttributeError as e:
            import traceback
            traceback.print_exc()
            return jsonify({
                "error": f"Model attribute error: {str(e)}. Please ensure models are trained."
            }), 500
        except ValueError as e:
            return jsonify({
                "error": f"Invalid input for prediction: {str(e)}"
            }), 400
        except Exception as e:
            import traceback
            error_trace = traceback.format_exc()
            print(f"❌ Prediction error details: {error_trace}")
            return jsonify({
                "error": f"Prediction error: {str(e)}"
            }), 500

        # Get comprehensive assessment
        assessment = chatbot.risk_assessor.get_comprehensive_assessment(
            stress_level=stress_level,
            bmi=bmi,
            physical_activity=physical_activity,
            sleep_hours=sleep_hours
        )

        # Generate guidance
        guidance = chatbot.guidance_generator.generate_comprehensive_guidance(assessment)
        summary = chatbot.risk_assessor.get_risk_summary(assessment)

        # Format final response
        final_reply = (
            f"🧠 **Stress Level:** {stress_level.upper()}\n\n"
            f"{summary}\n\n"
            f"{guidance}\n\n"
            "⚠️ This is educational only, not medical advice."
        )

        # Structured health data for Supabase (frontend saves when user is logged in)
        health_data = {
            "stress_level": stress_level,
            "sleep_hours": int(sleep_hours),
            "bmi": round(bmi, 2),
            "activity_level": physical_activity,
            "health_risks": summary,
        }

        # cleanup session
        del sessions[session_id]

        return jsonify({
            "reply": final_reply,
            "session_id": None,
            "health_data": health_data,
        })

    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print(f"❌ Error in chat endpoint: {error_trace}")
        return jsonify({
            "error": f"An error occurred: {str(e)}"
        }), 500


if __name__ == "__main__":
    print("🚀 Backend running on http://localhost:5001")
    print("📝 Frontend should connect to: http://localhost:5001")
    app.run(host="0.0.0.0", port=5001, debug=True)
