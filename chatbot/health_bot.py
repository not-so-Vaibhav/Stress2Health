"""
AI Health Chatbot - Web-Compatible Version
Combines NLP, ML, and rule-based systems for health analysis
"""

import sys
import os

# Add project root to path for imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from nlp.text_processor import TextProcessor
from nlp.ml_predictor import StressPredictor
from rules.disease_risk import DiseaseRiskAssessor
from rules.health_guidance import HealthGuidanceGenerator


class HealthChatbot:
    """
    Web-compatible AI Health Chatbot
    Uses step-based conversation instead of input()/print()
    """

    def __init__(self, model_type="logistic", use_deep_learning=False):
        self.text_processor = TextProcessor()
        self.risk_assessor = DiseaseRiskAssessor()
        self.guidance_generator = HealthGuidanceGenerator()

        self.use_deep_learning = use_deep_learning
        if use_deep_learning:
            from nlp.deep_predictor import DeepStressPredictor
            self.stress_predictor = DeepStressPredictor()
            self.stress_predictor.load_model("models/deep_learning")
        else:
            self.stress_predictor = StressPredictor(model_type=model_type)
            self.stress_predictor.load_model(f"models/{model_type}")

    # -----------------------------
    # SESSION HANDLING
    # -----------------------------
    def create_new_session(self):
        return {
            "step": 0,
            "data": {}
        }

    # -----------------------------
    # MAIN CONVERSATION ENGINE
    # -----------------------------
    def process_message(self, user_input, session):
        step = session["step"]
        data = session["data"]

        # STEP 0 — greeting
        if step == 0:
            session["step"] = 1
            return (
                "Hello 👋 I’m your AI Health Assistant.\n"
                "How are you feeling today? (stress, mood, concerns)",
                False
            )

        # STEP 1 — stress text
        if step == 1:
            data["text_input"] = user_input
            data["text_stress_level"] = self.text_processor.predict_stress_from_text(user_input)
            session["step"] = 2
            return "How many hours do you sleep per night?", False

        # STEP 2 — sleep
        if step == 2:
            try:
                sleep_hours = float(user_input)
                if sleep_hours < 0 or sleep_hours > 24:
                    return "Please enter a valid number of sleep hours (0-24):", False
                data["sleep_hours"] = sleep_hours
                session["step"] = 3
                return "What is your BMI?", False
            except ValueError:
                return "Please enter a valid number for sleep hours:", False

        # STEP 3 — BMI
        if step == 3:
            try:
                bmi = float(user_input)
                if bmi < 10 or bmi > 50:
                    return "Please enter a valid BMI (typically 10-50):", False
                data["bmi"] = bmi
                session["step"] = 4
                return "What is your physical activity level? (low / medium / high)", False
            except ValueError:
                return "Please enter a valid number for BMI:", False

        # STEP 4 — activity
        if step == 4:
            activity = user_input.lower().strip()
            if activity not in ['low', 'medium', 'high']:
                return "Please enter 'low', 'medium', or 'high' for physical activity level:", False
            data["physical_activity"] = activity
            session["step"] = 5
            return "How many hours do you work per day?", False

        # STEP 5 — work hours
        if step == 5:
            try:
                work_hours = float(user_input)
                if work_hours < 0 or work_hours > 24:
                    return "Please enter a valid number of work hours (0-24):", False
                data["work_hours"] = work_hours
                session["step"] = 6
                return "What is your social interaction level? (low / medium / high)", False
            except ValueError:
                return "Please enter a valid number for work hours:", False

        # STEP 6 — social
        if step == 6:
            social = user_input.lower().strip()
            if social not in ['low', 'medium', 'high']:
                return "Please enter 'low', 'medium', or 'high' for social interaction level:", False
            data["social_interaction"] = social

            # ---- ANALYSIS PHASE ----
            stress_level = self.stress_predictor.predict(
                sleep_hours=data["sleep_hours"],
                physical_activity=data["physical_activity"],
                work_hours=data["work_hours"],
                social_interaction=data["social_interaction"]
            )

            assessment = self.risk_assessor.get_comprehensive_assessment(
                stress_level=stress_level,
                bmi=data["bmi"],
                physical_activity=data["physical_activity"],
                sleep_hours=data["sleep_hours"]
            )

            guidance = self.guidance_generator.generate_comprehensive_guidance(assessment)
            summary = self.risk_assessor.get_risk_summary(assessment)

            final_reply = (
                f"🧠 **Stress Level:** {stress_level.upper()}\n\n"
                f"{summary}\n\n"
                f"{guidance}\n\n"
                "⚠️ This is educational only, not medical advice."
            )

            return final_reply, True  # conversation done
