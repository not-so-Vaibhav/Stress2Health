"""
Deep Learning Stress Predictor Module (Optional)
This module uses TensorFlow/Keras to build a neural network
for stress prediction as an advanced alternative to traditional ML.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os

try:
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout
    from tensorflow.keras.utils import to_categorical
    TENSORFLOW_AVAILABLE = True
except ImportError:
    TENSORFLOW_AVAILABLE = False
    print("TensorFlow not available. Install with: pip install tensorflow")


class DeepStressPredictor:
    """
    Deep Learning-based stress prediction using Neural Networks
    """
    
    def __init__(self):
        """
        Initialize deep learning stress predictor
        """
        if not TENSORFLOW_AVAILABLE:
            raise ImportError("TensorFlow is required for DeepStressPredictor")
        
        self.model = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.n_classes = 3  # low, medium, high
    
    def build_model(self, input_dim):
        """
        Build neural network architecture
        
        Args:
            input_dim (int): Number of input features
            
        Returns:
            Sequential: Keras model
        """
        model = Sequential([
            Dense(64, activation='relu', input_dim=input_dim),
            Dropout(0.3),
            Dense(32, activation='relu'),
            Dropout(0.2),
            Dense(16, activation='relu'),
            Dense(self.n_classes, activation='softmax')
        ])
        
        model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
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
    
    def train(self, data_path, epochs=50, batch_size=8, validation_split=0.2):
        """
        Train the deep learning model
        
        Args:
            data_path (str): Path to training data CSV
            epochs (int): Number of training epochs
            batch_size (int): Batch size for training
            validation_split (float): Validation data split ratio
            
        Returns:
            dict: Training history and metrics
        """
        print("Training Deep Learning model...")
        
        # Load data
        df = pd.read_csv(data_path)
        
        # Prepare features
        X, y = self.prepare_features(df)
        
        # Encode labels
        y_encoded = self.label_encoder.fit_transform(y)
        y_categorical = to_categorical(y_encoded, num_classes=self.n_classes)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_categorical, test_size=0.2, random_state=42
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Build model
        self.model = self.build_model(input_dim=X_train.shape[1])
        
        print("\nModel Architecture:")
        self.model.summary()
        
        # Train model
        history = self.model.fit(
            X_train_scaled, y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=validation_split,
            verbose=1
        )
        
        # Evaluate model
        test_loss, test_accuracy = self.model.evaluate(X_test_scaled, y_test, verbose=0)
        
        print(f"\n{'='*50}")
        print(f"Model: Deep Neural Network")
        print(f"Test Accuracy: {test_accuracy:.2%}")
        print(f"Test Loss: {test_loss:.4f}")
        print(f"{'='*50}\n")
        
        metrics = {
            'accuracy': test_accuracy,
            'loss': test_loss,
            'history': history.history,
            'n_samples': len(df)
        }
        
        return metrics
    
    def predict(self, sleep_hours, physical_activity, work_hours, social_interaction):
        """
        Predict stress level for given inputs
        
        Args:
            sleep_hours (float): Hours of sleep
            physical_activity (str): Activity level ('low', 'medium', 'high')
            work_hours (float): Hours of work
            social_interaction (str): Social interaction level
            
        Returns:
            str: Predicted stress level
        """
        # Map activity levels
        activity_mapping = {'low': 0, 'medium': 1, 'high': 2}
        
        # Prepare input
        X = np.array([[
            sleep_hours,
            activity_mapping[physical_activity.lower()],
            work_hours,
            activity_mapping[social_interaction.lower()]
        ]])
        
        # Scale input
        X_scaled = self.scaler.transform(X)
        
        # Predict
        prediction = self.model.predict(X_scaled, verbose=0)
        predicted_class = np.argmax(prediction, axis=1)[0]
        
        # Decode prediction
        stress_level = self.label_encoder.inverse_transform([predicted_class])[0]
        
        return stress_level
    
    def get_prediction_probability(self, sleep_hours, physical_activity, 
                                   work_hours, social_interaction):
        """
        Get prediction probabilities for all classes
        
        Args:
            Similar to predict method
            
        Returns:
            dict: Probabilities for each stress level
        """
        # Map activity levels
        activity_mapping = {'low': 0, 'medium': 1, 'high': 2}
        
        # Prepare input
        X = np.array([[
            sleep_hours,
            activity_mapping[physical_activity.lower()],
            work_hours,
            activity_mapping[social_interaction.lower()]
        ]])
        
        # Scale input
        X_scaled = self.scaler.transform(X)
        
        # Get probabilities
        probabilities = self.model.predict(X_scaled, verbose=0)[0]
        
        # Create dictionary
        prob_dict = {
            level: float(prob) for level, prob in 
            zip(self.label_encoder.classes_, probabilities)
        }
        
        return prob_dict
    
    def save_model(self, model_dir):
        """
        Save trained model and preprocessing objects
        
        Args:
            model_dir (str): Directory to save model
        """
        os.makedirs(model_dir, exist_ok=True)
        
        self.model.save(os.path.join(model_dir, 'deep_learning_model.h5'))
        joblib.dump(self.scaler, os.path.join(model_dir, 'scaler.pkl'))
        joblib.dump(self.label_encoder, os.path.join(model_dir, 'label_encoder.pkl'))
        
        print(f"Model saved to {model_dir}")
    
    def load_model(self, model_dir):
        """
        Load trained model and preprocessing objects
        
        Args:
            model_dir (str): Directory containing saved model
        """
        self.model = keras.models.load_model(
            os.path.join(model_dir, 'deep_learning_model.h5')
        )
        self.scaler = joblib.load(os.path.join(model_dir, 'scaler.pkl'))
        self.label_encoder = joblib.load(os.path.join(model_dir, 'label_encoder.pkl'))
        
        print(f"Model loaded from {model_dir}")


# Example usage and training script
if __name__ == "__main__":
    if TENSORFLOW_AVAILABLE:
        print(f"\n{'#'*60}")
        print(f"Training Deep Learning Neural Network")
        print(f"{'#'*60}")
        
        predictor = DeepStressPredictor()
        metrics = predictor.train('../data/stress_dataset.csv', epochs=50)
        predictor.save_model('../models/deep_learning')
        
        # Test prediction
        stress_level = predictor.predict(
            sleep_hours=5,
            physical_activity='low',
            work_hours=11,
            social_interaction='low'
        )
        print(f"Test Prediction: {stress_level}")
        
        # Test probabilities
        probs = predictor.get_prediction_probability(
            sleep_hours=5,
            physical_activity='low',
            work_hours=11,
            social_interaction='low'
        )
        print(f"Prediction Probabilities: {probs}")
    else:
        print("TensorFlow not available. Skipping deep learning model training.")