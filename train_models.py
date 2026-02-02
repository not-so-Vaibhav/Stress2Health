"""
Model Training Script
This script trains all ML models (Logistic Regression, Decision Tree, Random Forest)
and optionally the Deep Learning model.
"""

import os
import sys

# Ensure we can import from parent directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from nlp.ml_predictor import StressPredictor


def train_ml_models():
    """
    Train all traditional ML models
    """
    print("\n" + "="*70)
    print("🚀 TRAINING MACHINE LEARNING MODELS")
    print("="*70 + "\n")
    
    models_trained = []
    
    # Train each model type
    for model_type in ['logistic', 'decision_tree', 'random_forest']:
        try:
            print(f"\n{'#'*70}")
            print(f"📊 Training {model_type.upper().replace('_', ' ')} model")
            print(f"{'#'*70}\n")
            
            # Initialize predictor
            predictor = StressPredictor(model_type=model_type)
            
            # Train model
            metrics = predictor.train('data/stress_dataset.csv')
            
            # Save model
            predictor.save_model(f'models/{model_type}')
            
            # Test prediction
            print(f"\n✅ Testing {model_type} model...")
            test_stress = predictor.predict(
                sleep_hours=5,
                physical_activity='low',
                work_hours=11,
                social_interaction='low'
            )
            print(f"   Test prediction (high stress profile): {test_stress}")
            
            test_stress2 = predictor.predict(
                sleep_hours=8,
                physical_activity='high',
                work_hours=7,
                social_interaction='high'
            )
            print(f"   Test prediction (low stress profile): {test_stress2}")
            
            models_trained.append(model_type)
            print(f"\n✅ {model_type.upper()} model trained and saved successfully!")
            
        except Exception as e:
            print(f"\n❌ Error training {model_type} model: {e}")
            import traceback
            traceback.print_exc()
    
    return models_trained


def train_deep_learning_model():
    """
    Train deep learning model (optional)
    """
    print("\n" + "="*70)
    print("🚀 TRAINING DEEP LEARNING MODEL (OPTIONAL)")
    print("="*70 + "\n")
    
    try:
        from nlp.deep_predictor import DeepStressPredictor, TENSORFLOW_AVAILABLE
        
        if not TENSORFLOW_AVAILABLE:
            print("⚠️  TensorFlow not installed. Skipping deep learning model.")
            print("To use deep learning, install TensorFlow:")
            print("   pip install tensorflow")
            return False
        
        print("📊 Training Neural Network...\n")
        
        # Initialize predictor
        predictor = DeepStressPredictor()
        
        # Train model
        metrics = predictor.train('data/stress_dataset.csv', epochs=50)
        
        # Save model
        predictor.save_model('models/deep_learning')
        
        # Test prediction
        print("\n✅ Testing deep learning model...")
        test_stress = predictor.predict(
            sleep_hours=5,
            physical_activity='low',
            work_hours=11,
            social_interaction='low'
        )
        print(f"   Test prediction (high stress profile): {test_stress}")
        
        test_stress2 = predictor.predict(
            sleep_hours=8,
            physical_activity='high',
            work_hours=7,
            social_interaction='high'
        )
        print(f"   Test prediction (low stress profile): {test_stress2}")
        
        print("\n✅ Deep learning model trained and saved successfully!")
        return True
        
    except Exception as e:
        print(f"\n❌ Error training deep learning model: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """
    Main training function
    """
    print("\n" + "="*70)
    print("🏥 AI HEALTH CHATBOT - MODEL TRAINING")
    print("="*70)
    print("\nThis script will train all machine learning models for stress prediction.")
    print("Training time: ~1-2 minutes for ML models, ~5-10 minutes for DL model")
    print("\n" + "="*70 + "\n")
    
    # Create models directory
    os.makedirs('models', exist_ok=True)
    
    # Check if data exists
    if not os.path.exists('data/stress_dataset.csv'):
        print("❌ Error: Training data not found!")
        print("Expected file: data/stress_dataset.csv")
        print("\nPlease ensure the data file exists before training.")
        sys.exit(1)
    
    # Train ML models
    ml_models = train_ml_models()
    
    # Ask about deep learning
    print("\n" + "="*70)
    print("\nWould you like to train the deep learning model? (yes/no)")
    print("Note: This requires TensorFlow and takes longer to train.")
    response = input("→ ").strip().lower()
    
    dl_trained = False
    if response in ['yes', 'y']:
        dl_trained = train_deep_learning_model()
    else:
        print("\n⏭️  Skipping deep learning model training.")
    
    # Summary
    print("\n" + "="*70)
    print("📊 TRAINING SUMMARY")
    print("="*70)
    print(f"\n✅ ML Models Trained: {len(ml_models)}")
    for model in ml_models:
        print(f"   • {model}")
    
    if dl_trained:
        print(f"\n✅ Deep Learning Model: Trained")
    else:
        print(f"\n⏭️  Deep Learning Model: Skipped")
    
    print("\n" + "="*70)
    print("\n🎉 Training Complete!")
    print("\nYou can now run the chatbot with:")
    print("   python app.py")
    print("\nOr use the chatbot module directly:")
    print("   python chatbot/health_bot.py")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Training interrupted by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()