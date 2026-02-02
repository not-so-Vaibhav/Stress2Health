"""
Health Guidance Generator Module
This module generates personalized preventive health guidance
based on risk assessment results.
"""


class HealthGuidanceGenerator:
    """
    Generate personalized health guidance based on risk factors
    """
    
    def __init__(self):
        """
        Initialize health guidance generator with recommendation templates
        """
        self.stress_management_tips = {
            'high': [
                "Practice deep breathing exercises for 10 minutes daily",
                "Consider mindfulness meditation or yoga",
                "Establish a consistent sleep schedule",
                "Limit caffeine and alcohol intake",
                "Take regular breaks during work",
                "Engage in physical activities you enjoy",
                "Consider professional counseling or therapy",
                "Practice progressive muscle relaxation",
                "Maintain a stress journal to identify triggers",
                "Connect with supportive friends and family"
            ],
            'medium': [
                "Engage in regular physical exercise (30 minutes daily)",
                "Practice time management techniques",
                "Take short breaks during stressful tasks",
                "Maintain work-life balance",
                "Try relaxation techniques like deep breathing",
                "Ensure adequate sleep (7-8 hours)",
                "Limit exposure to stressful situations when possible"
            ],
            'low': [
                "Maintain your current healthy lifestyle",
                "Continue regular exercise routine",
                "Keep up good sleep habits",
                "Stay socially connected"
            ]
        }
        
        self.disease_specific_guidance = {
            'diabetes': {
                'high': [
                    "Schedule a medical check-up and HbA1c test",
                    "Monitor your blood glucose levels regularly",
                    "Follow a low-glycemic diet (reduce refined sugars)",
                    "Increase fiber intake (whole grains, vegetables)",
                    "Engage in 150 minutes of moderate exercise weekly",
                    "Maintain a healthy weight (BMI 18.5-24.9)",
                    "Stay hydrated throughout the day"
                ],
                'medium': [
                    "Reduce sugar and refined carbohydrate intake",
                    "Include more vegetables and lean proteins",
                    "Exercise regularly (at least 30 minutes daily)",
                    "Monitor your weight and BMI",
                    "Consider annual diabetes screening"
                ],
                'low': [
                    "Maintain balanced diet with limited processed foods",
                    "Stay physically active",
                    "Monitor your health during annual check-ups"
                ]
            },
            'blood_pressure': {
                'high': [
                    "Consult a doctor for blood pressure monitoring",
                    "Reduce sodium intake (less than 2,300mg daily)",
                    "Follow the DASH diet (fruits, vegetables, whole grains)",
                    "Limit alcohol consumption",
                    "Quit smoking if applicable",
                    "Manage stress through relaxation techniques",
                    "Exercise regularly (aerobic activities preferred)",
                    "Maintain healthy weight"
                ],
                'medium': [
                    "Monitor blood pressure regularly at home",
                    "Reduce salt in your diet",
                    "Increase potassium-rich foods (bananas, spinach)",
                    "Exercise 30 minutes most days of the week",
                    "Manage stress effectively"
                ],
                'low': [
                    "Continue healthy eating habits",
                    "Maintain regular physical activity",
                    "Keep stress levels manageable"
                ]
            },
            'obesity': {
                'high': [
                    "Consult a healthcare provider or nutritionist",
                    "Set realistic weight loss goals (1-2 pounds per week)",
                    "Create a balanced meal plan with portion control",
                    "Engage in regular physical activity (start gradually)",
                    "Keep a food diary to track eating patterns",
                    "Avoid crash diets and focus on sustainable changes",
                    "Get adequate sleep (7-9 hours)",
                    "Address emotional eating patterns"
                ],
                'medium': [
                    "Increase physical activity levels gradually",
                    "Practice mindful eating and portion control",
                    "Choose whole foods over processed options",
                    "Reduce sugary drinks and snacks",
                    "Find enjoyable forms of exercise"
                ],
                'low': [
                    "Maintain current healthy weight",
                    "Continue balanced diet and exercise routine",
                    "Monitor weight periodically"
                ]
            },
            'cardiovascular': {
                'high': [
                    "Schedule comprehensive cardiac evaluation",
                    "Adopt heart-healthy diet (Mediterranean diet)",
                    "Quit smoking immediately if applicable",
                    "Exercise regularly (after medical clearance)",
                    "Manage blood pressure and cholesterol",
                    "Reduce saturated and trans fats",
                    "Increase omega-3 fatty acids (fish, nuts)",
                    "Maintain healthy weight",
                    "Manage stress and get quality sleep"
                ],
                'medium': [
                    "Include heart-healthy foods in diet",
                    "Exercise moderately 150 minutes per week",
                    "Reduce red meat consumption",
                    "Monitor cholesterol levels annually",
                    "Manage stress effectively"
                ],
                'low': [
                    "Continue heart-healthy lifestyle",
                    "Stay physically active",
                    "Maintain healthy diet"
                ]
            },
            'sleep_disorder': {
                'high': [
                    "Consult a sleep specialist for evaluation",
                    "Establish consistent sleep-wake schedule",
                    "Create optimal sleep environment (dark, quiet, cool)",
                    "Avoid screens 1-2 hours before bedtime",
                    "Limit caffeine after 2 PM",
                    "Avoid large meals close to bedtime",
                    "Practice relaxation techniques before sleep",
                    "Consider cognitive behavioral therapy for insomnia",
                    "Limit daytime napping"
                ],
                'medium': [
                    "Improve sleep hygiene practices",
                    "Maintain regular sleep schedule",
                    "Create relaxing bedtime routine",
                    "Limit screen time before bed",
                    "Ensure bedroom is comfortable for sleep"
                ],
                'low': [
                    "Maintain good sleep habits",
                    "Keep consistent sleep schedule",
                    "Practice relaxation before bed"
                ]
            }
        }
    
    def generate_stress_guidance(self, stress_level):
        """
        Generate stress management guidance
        
        Args:
            stress_level (str): Stress level ('low', 'medium', 'high')
            
        Returns:
            list: List of stress management recommendations
        """
        return self.stress_management_tips.get(stress_level, [])
    
    def generate_disease_guidance(self, disease, risk_level):
        """
        Generate disease-specific guidance
        
        Args:
            disease (str): Disease name
            risk_level (str): Risk level ('low', 'medium', 'high')
            
        Returns:
            list: List of disease-specific recommendations
        """
        disease_key = disease.lower().replace(' ', '_').replace('_risk', '')
        return self.disease_specific_guidance.get(disease_key, {}).get(risk_level, [])
    
    def generate_comprehensive_guidance(self, risk_assessment):
        """
        Generate comprehensive health guidance based on all risk factors
        
        Args:
            risk_assessment (dict): Dictionary of risk assessments
            
        Returns:
            str: Formatted guidance text
        """
        guidance = "\n" + "="*60 + "\n"
        guidance += "🌟 PERSONALIZED HEALTH GUIDANCE\n"
        guidance += "="*60 + "\n\n"
        
        # Medical disclaimer
        guidance += "⚠️  MEDICAL DISCLAIMER:\n"
        guidance += "-" * 60 + "\n"
        guidance += "This is AI-generated guidance for INFORMATIONAL purposes only.\n"
        guidance += "It is NOT a medical diagnosis or treatment recommendation.\n"
        guidance += "Please consult healthcare professionals for proper diagnosis\n"
        guidance += "and treatment of any health conditions.\n"
        guidance += "-" * 60 + "\n\n"
        
        # Stress management
        stress_level = risk_assessment.get('overall_stress', 'medium')
        guidance += "🧠 STRESS MANAGEMENT RECOMMENDATIONS:\n"
        guidance += "-" * 60 + "\n"
        stress_tips = self.generate_stress_guidance(stress_level)
        for i, tip in enumerate(stress_tips[:5], 1):
            guidance += f"{i}. {tip}\n"
        guidance += "\n"
        
        # Disease-specific guidance for high and medium risks
        high_risk_diseases = [k for k, v in risk_assessment.items() 
                             if k.endswith('_risk') and v == 'high']
        medium_risk_diseases = [k for k, v in risk_assessment.items() 
                               if k.endswith('_risk') and v == 'medium']
        
        if high_risk_diseases:
            guidance += "🚨 HIGH PRIORITY RECOMMENDATIONS:\n"
            guidance += "-" * 60 + "\n"
            for disease in high_risk_diseases:
                disease_name = disease.replace('_risk', '').replace('_', ' ').title()
                guidance += f"\n📍 {disease_name}:\n"
                recommendations = self.generate_disease_guidance(disease, 'high')
                for i, rec in enumerate(recommendations[:5], 1):
                    guidance += f"   {i}. {rec}\n"
            guidance += "\n"
        
        if medium_risk_diseases:
            guidance += "⚡ PREVENTIVE CARE RECOMMENDATIONS:\n"
            guidance += "-" * 60 + "\n"
            for disease in medium_risk_diseases:
                disease_name = disease.replace('_risk', '').replace('_', ' ').title()
                guidance += f"\n📍 {disease_name}:\n"
                recommendations = self.generate_disease_guidance(disease, 'medium')
                for i, rec in enumerate(recommendations[:4], 1):
                    guidance += f"   {i}. {rec}\n"
            guidance += "\n"
        
        # General wellness tips
        guidance += "💪 GENERAL WELLNESS TIPS:\n"
        guidance += "-" * 60 + "\n"
        guidance += "1. Drink 8-10 glasses of water daily\n"
        guidance += "2. Eat a balanced diet with fruits and vegetables\n"
        guidance += "3. Get 7-9 hours of quality sleep\n"
        guidance += "4. Exercise for at least 30 minutes daily\n"
        guidance += "5. Practice stress management techniques\n"
        guidance += "6. Schedule regular health check-ups\n"
        guidance += "7. Avoid smoking and limit alcohol\n"
        guidance += "8. Maintain social connections\n\n"
        
        # Action items
        guidance += "✅ IMMEDIATE ACTION ITEMS:\n"
        guidance += "-" * 60 + "\n"
        if high_risk_diseases:
            guidance += "• Schedule appointment with healthcare provider\n"
            guidance += "• Start tracking relevant health metrics\n"
        guidance += "• Begin implementing one new healthy habit this week\n"
        guidance += "• Set achievable short-term health goals\n"
        guidance += "• Create a support system for lifestyle changes\n\n"
        
        guidance += "="*60 + "\n"
        guidance += "Remember: Small, consistent changes lead to big results!\n"
        guidance += "Take it one step at a time. 🌱\n"
        guidance += "="*60 + "\n"
        
        return guidance
    
    def generate_quick_tips(self, risk_assessment):
        """
        Generate quick, actionable tips based on top priorities
        
        Args:
            risk_assessment (dict): Dictionary of risk assessments
            
        Returns:
            list: List of quick tips (3-5 items)
        """
        tips = []
        
        # Based on stress level
        stress_level = risk_assessment.get('overall_stress', 'medium')
        if stress_level == 'high':
            tips.append("Start with 5-minute breathing exercises today")
        
        # Based on BMI
        bmi_category = risk_assessment.get('bmi_category', 'normal')
        if bmi_category in ['overweight', 'obese']:
            tips.append("Add one extra serving of vegetables to your meals")
        
        # Based on sleep
        if risk_assessment.get('sleep_disorder_risk') == 'high':
            tips.append("Set a consistent bedtime starting tonight")
        
        # Based on cardiovascular risk
        if risk_assessment.get('cardiovascular_risk') == 'high':
            tips.append("Take a 10-minute walk after meals")
        
        # General tip
        tips.append("Drink a glass of water first thing in the morning")
        
        return tips[:5]


# Example usage
if __name__ == "__main__":
    generator = HealthGuidanceGenerator()
    
    # Test comprehensive guidance
    test_assessment = {
        'diabetes_risk': 'high',
        'blood_pressure_risk': 'medium',
        'obesity_risk': 'high',
        'cardiovascular_risk': 'medium',
        'sleep_disorder_risk': 'high',
        'bmi_category': 'obese',
        'overall_stress': 'high'
    }
    
    guidance = generator.generate_comprehensive_guidance(test_assessment)
    print(guidance)
    
    print("\n\nQUICK TIPS:")
    tips = generator.generate_quick_tips(test_assessment)
    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")