"""
Machine Learning Stress Predictor Module
This module trains and uses ML models (Logistic Regression, Decision Tree)
to predict stress levels based on lifestyle and text features.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os
from pathlib import Path  # ✅ ADDED (ONLY NEW IMPORT)


class StressPredictor:
    """
    ML-based stress prediction class
    """
    
    def __init__(self, model_type='logistic'):
        """
        Initialize stress predictor
        
        Args:
            model_type (str): Type of model ('logistic', 'decision_tree', 'random_forest')
        """
        self.model_type = model_type
        self.model = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        
        # Initialize model based on type
        if model_type == 'logistic':
            self.model = LogisticRegression(random_state=42, max_iter=1000)
        elif model_type == 'decision_tree':
            self.model = DecisionTreeClassifier(random_state=42, max_depth=5)
        elif model_type == 'random_forest':
            self.model = RandomForestClassifier(random_state=42, n_estimators=100)
        else:
            raise ValueError(f"Unknown model type: {model_type}")
    
    def prepare_features(self, df):
        """
        Prepare features from dataframe
        
        Args:
            df (DataFrame): Input dataframe
            
        Returns:
            tuple: (X, y) features and labels
        """
        # Encode categorical variables
        activity_mapping = {'low': 0, 'medium': 1, 'high': 2}
        
        # Create feature columns
        X = pd.DataFrame()
        X['sleep_hours'] = df['sleep_hours']
        X['physical_activity'] = df['physical_activity'].map(activity_mapping)
        X['work_hours'] = df['work_hours']
        X['social_interaction'] = df['social_interaction'].map(activity_mapping)
        
        # Target variable
        y = df['stress_level']
        
        return X, y
    
    def train(self, data_path):
        """
        Train the stress prediction model
        
        Args:
            data_path (str): Path to training data CSV
            
        Returns:
            dict: Training metrics
        """
        print(f"Training {self.model_type} model...")
        
        # Load data
        df = pd.read_csv(data_path)
        
        # Prepare features
        X, y = self.prepare_features(df)
        
        # Encode labels
        y_encoded = self.label_encoder.fit_transform(y)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_encoded, test_size=0.2, random_state=42,
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        self.model.fit(X_train_scaled, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"\n{'='*50}")
        print(f"Model: {self.model_type}")
        print(f"Accuracy: {accuracy:.2%}")
        print(f"\nClassification Report:")
        print(classification_report(
            y_test,
            y_pred,
            zero_division=0
        ))
        print(f"{'='*50}\n")
        
        metrics = {
            'accuracy': accuracy,
            'model_type': self.model_type,
            'n_samples': len(df)
        }
        
        return metrics
    
    def predict(self, sleep_hours, physical_activity, work_hours, social_interaction):
        """
        Predict stress level for given inputs
        """
        activity_mapping = {'low': 0, 'medium': 1, 'high': 2}
        
        X = pd.DataFrame([{
            'sleep_hours': sleep_hours,
            'physical_activity': activity_mapping[physical_activity.lower()],
            'work_hours': work_hours,
            'social_interaction': activity_mapping[social_interaction.lower()]
        }])
        
        X_scaled = self.scaler.transform(X)
        prediction = self.model.predict(X_scaled)
        
        stress_level = self.label_encoder.inverse_transform(prediction)[0]
        return stress_level
    
    def get_prediction_probability(self, sleep_hours, physical_activity, 
                                   work_hours, social_interaction):
        """
        Get prediction probabilities for all classes
        """
        activity_mapping = {'low': 0, 'medium': 1, 'high': 2}
        
        X = pd.DataFrame([{
            'sleep_hours': sleep_hours,
            'physical_activity': activity_mapping[physical_activity.lower()],
            'work_hours': work_hours,
            'social_interaction': activity_mapping[social_interaction.lower()]
        }])
        
        X_scaled = self.scaler.transform(X)
        probabilities = self.model.predict_proba(X_scaled)[0]
        
        prob_dict = {
            level: prob for level, prob in 
            zip(self.label_encoder.classes_, probabilities)
        }
        
        return prob_dict
    
    # ===================== FIXED PATH HANDLING =====================
    
    def save_model(self, model_dir):
        """
        Save trained model and preprocessing objects
        """
        BASE_DIR = Path(__file__).resolve().parent.parent  # Stress2Health/
        model_dir = BASE_DIR / model_dir
        
        os.makedirs(model_dir, exist_ok=True)
        
        joblib.dump(self.model, model_dir / f'{self.model_type}_model.pkl')
        joblib.dump(self.scaler, model_dir / 'scaler.pkl')
        joblib.dump(self.label_encoder, model_dir / 'label_encoder.pkl')
        
        print(f"Model saved to {model_dir}")
    
    def load_model(self, model_dir):
        """
        Load trained model and preprocessing objects
        """
        BASE_DIR = Path(__file__).resolve().parent.parent  # Stress2Health/
        model_dir = BASE_DIR / model_dir
        
        self.model = joblib.load(model_dir / f'{self.model_type}_model.pkl')
        self.scaler = joblib.load(model_dir / 'scaler.pkl')
        self.label_encoder = joblib.load(model_dir / 'label_encoder.pkl')
        
        print(f"Model loaded from {model_dir}")


# ==========================================================
# Example usage and training script
# ==========================================================

if __name__ == "__main__":
    for model_type in ['logistic', 'decision_tree', 'random_forest']:
        print(f"\n{'#'*60}")
        print(f"Training {model_type.upper()} model")
        print(f"{'#'*60}")
        
        predictor = StressPredictor(model_type=model_type)
        metrics = predictor.train('data/stress_dataset.csv')
        predictor.save_model(f'models/{model_type}')
        
        stress_level = predictor.predict(
            sleep_hours=5,
            physical_activity='low',
            work_hours=11,
            social_interaction='low'
        )
        print(f"Test Prediction: {stress_level}")
