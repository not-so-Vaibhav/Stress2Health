"""
Rule-Based Disease Risk Assessment Module
This module implements a rule-based system to assess the risk of lifestyle diseases
based on stress levels, BMI, sleep patterns, and physical activity.
"""


class DiseaseRiskAssessor:
    """
    Rule-based system for assessing disease risks based on lifestyle factors
    """
    
    def __init__(self):
        """
        Initialize disease risk assessor with risk thresholds
        """
        # BMI categories
        self.bmi_categories = {
            'underweight': (0, 18.5),
            'normal': (18.5, 25),
            'overweight': (25, 30),
            'obese': (30, float('inf'))
        }
        
        # Risk level mapping
        self.risk_levels = ['low', 'medium', 'high']
    
    def get_bmi_category(self, bmi):
        """
        Determine BMI category
        
        Args:
            bmi (float): Body Mass Index value
            
        Returns:
            str: BMI category
        """
        for category, (lower, upper) in self.bmi_categories.items():
            if lower <= bmi < upper:
                return category
        return 'normal'
    
    def assess_diabetes_risk(self, stress_level, bmi, physical_activity, sleep_hours):
        """
        Assess diabetes risk based on multiple factors
        
        Args:
            stress_level (str): Stress level ('low', 'medium', 'high')
            bmi (float): Body Mass Index
            physical_activity (str): Activity level
            sleep_hours (float): Average sleep hours
            
        Returns:
            str: Risk level ('low', 'medium', 'high')
        """
        risk_score = 0
        
        # BMI contribution
        if bmi >= 30:
            risk_score += 3
        elif bmi >= 25:
            risk_score += 2
        elif bmi < 18.5:
            risk_score += 1
        
        # Stress contribution
        if stress_level == 'high':
            risk_score += 2
        elif stress_level == 'medium':
            risk_score += 1
        
        # Physical activity contribution
        if physical_activity == 'low':
            risk_score += 2
        elif physical_activity == 'medium':
            risk_score += 1
        
        # Sleep contribution
        if sleep_hours < 6 or sleep_hours > 9:
            risk_score += 1
        
        # Determine risk level
        if risk_score >= 6:
            return 'high'
        elif risk_score >= 3:
            return 'medium'
        else:
            return 'low'
    
    def assess_blood_pressure_risk(self, stress_level, bmi, physical_activity, sleep_hours):
        """
        Assess high blood pressure risk
        
        Args:
            Similar to assess_diabetes_risk
            
        Returns:
            str: Risk level
        """
        risk_score = 0
        
        # Stress is a major factor for BP
        if stress_level == 'high':
            risk_score += 3
        elif stress_level == 'medium':
            risk_score += 2
        
        # BMI contribution
        if bmi >= 30:
            risk_score += 2
        elif bmi >= 25:
            risk_score += 1
        
        # Physical activity
        if physical_activity == 'low':
            risk_score += 2
        elif physical_activity == 'medium':
            risk_score += 1
        
        # Sleep quality
        if sleep_hours < 6:
            risk_score += 2
        elif sleep_hours < 7:
            risk_score += 1
        
        if risk_score >= 6:
            return 'high'
        elif risk_score >= 3:
            return 'medium'
        else:
            return 'low'
    
    def assess_obesity_risk(self, bmi, physical_activity, sleep_hours, stress_level):
        """
        Assess obesity risk
        
        Args:
            Similar to previous methods
            
        Returns:
            str: Risk level
        """
        risk_score = 0
        
        # BMI is primary factor
        if bmi >= 30:
            return 'high'  # Already obese
        elif bmi >= 27:
            risk_score += 3
        elif bmi >= 25:
            risk_score += 2
        
        # Physical activity
        if physical_activity == 'low':
            risk_score += 2
        elif physical_activity == 'medium':
            risk_score += 1
        
        # Stress (stress eating)
        if stress_level == 'high':
            risk_score += 2
        elif stress_level == 'medium':
            risk_score += 1
        
        # Sleep (affects metabolism)
        if sleep_hours < 6 or sleep_hours > 9:
            risk_score += 1
        
        if risk_score >= 5:
            return 'high'
        elif risk_score >= 3:
            return 'medium'
        else:
            return 'low'
    
    def assess_cardiovascular_risk(self, stress_level, bmi, physical_activity, sleep_hours):
        """
        Assess cardiovascular disease risk
        
        Args:
            Similar to previous methods
            
        Returns:
            str: Risk level
        """
        risk_score = 0
        
        # Multiple factors contribute
        if stress_level == 'high':
            risk_score += 3
        elif stress_level == 'medium':
            risk_score += 1
        
        if bmi >= 30:
            risk_score += 3
        elif bmi >= 25:
            risk_score += 2
        
        if physical_activity == 'low':
            risk_score += 3
        elif physical_activity == 'medium':
            risk_score += 1
        
        if sleep_hours < 6:
            risk_score += 2
        
        if risk_score >= 7:
            return 'high'
        elif risk_score >= 4:
            return 'medium'
        else:
            return 'low'
    
    def assess_sleep_disorder_risk(self, stress_level, sleep_hours):
        """
        Assess sleep disorder risk
        
        Args:
            stress_level (str): Stress level
            sleep_hours (float): Average sleep hours
            
        Returns:
            str: Risk level
        """
        risk_score = 0
        
        # Sleep hours
        if sleep_hours < 5:
            risk_score += 3
        elif sleep_hours < 6:
            risk_score += 2
        elif sleep_hours < 7 or sleep_hours > 9:
            risk_score += 1
        
        # Stress strongly affects sleep
        if stress_level == 'high':
            risk_score += 3
        elif stress_level == 'medium':
            risk_score += 2
        
        if risk_score >= 4:
            return 'high'
        elif risk_score >= 2:
            return 'medium'
        else:
            return 'low'
    
    def get_comprehensive_assessment(self, stress_level, bmi, physical_activity, sleep_hours):
        """
        Get comprehensive risk assessment for all diseases
        
        Args:
            stress_level (str): Stress level
            bmi (float): Body Mass Index
            physical_activity (str): Activity level
            sleep_hours (float): Average sleep hours
            
        Returns:
            dict: Dictionary of risk assessments for each disease
        """
        assessment = {
            'diabetes_risk': self.assess_diabetes_risk(
                stress_level, bmi, physical_activity, sleep_hours
            ),
            'blood_pressure_risk': self.assess_blood_pressure_risk(
                stress_level, bmi, physical_activity, sleep_hours
            ),
            'obesity_risk': self.assess_obesity_risk(
                bmi, physical_activity, sleep_hours, stress_level
            ),
            'cardiovascular_risk': self.assess_cardiovascular_risk(
                stress_level, bmi, physical_activity, sleep_hours
            ),
            'sleep_disorder_risk': self.assess_sleep_disorder_risk(
                stress_level, sleep_hours
            ),
            'bmi_category': self.get_bmi_category(bmi),
            'overall_stress': stress_level
        }
        
        return assessment
    
    def get_risk_summary(self, assessment):
        """
        Generate a text summary of risk assessment
        
        Args:
            assessment (dict): Risk assessment dictionary
            
        Returns:
            str: Human-readable summary
        """
        high_risks = [k.replace('_risk', '').replace('_', ' ').title() 
                      for k, v in assessment.items() 
                      if k.endswith('_risk') and v == 'high']
        
        medium_risks = [k.replace('_risk', '').replace('_', ' ').title() 
                        for k, v in assessment.items() 
                        if k.endswith('_risk') and v == 'medium']
        
        summary = "\n🏥 HEALTH RISK ASSESSMENT SUMMARY\n"
        summary += "=" * 50 + "\n\n"
        
        if high_risks:
            summary += "⚠️  HIGH RISK CONDITIONS:\n"
            for risk in high_risks:
                summary += f"   • {risk}\n"
            summary += "\n"
        
        if medium_risks:
            summary += "⚡ MODERATE RISK CONDITIONS:\n"
            for risk in medium_risks:
                summary += f"   • {risk}\n"
            summary += "\n"
        
        if not high_risks and not medium_risks:
            summary += "✅ Good news! All risk levels are LOW.\n\n"
        
        summary += f"📊 BMI Category: {assessment['bmi_category'].title()}\n"
        summary += f"🧠 Stress Level: {assessment['overall_stress'].title()}\n"
        
        return summary


# Example usage
if __name__ == "__main__":
    assessor = DiseaseRiskAssessor()
    
    # Test case 1: High risk scenario
    print("Test Case 1: High Risk Profile")
    assessment1 = assessor.get_comprehensive_assessment(
        stress_level='high',
        bmi=31.5,
        physical_activity='low',
        sleep_hours=4.5
    )
    print(assessor.get_risk_summary(assessment1))
    
    # Test case 2: Low risk scenario
    print("\nTest Case 2: Low Risk Profile")
    assessment2 = assessor.get_comprehensive_assessment(
        stress_level='low',
        bmi=22.5,
        physical_activity='high',
        sleep_hours=8
    )
    print(assessor.get_risk_summary(assessment2))