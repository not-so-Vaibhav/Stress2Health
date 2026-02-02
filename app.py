"""
AI Health Chatbot - Main Application Entry Point
Run this file to start the chatbot application.
"""

import os
import sys

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chatbot.health_bot import HealthChatbot


def check_requirements():
    """
    Check if all required models and data are available
    """
    issues = []
    
    # Check for trained models
    if not os.path.exists('models/logistic/logistic_model.pkl'):
        issues.append("ML models not trained")
    
    # Check for data
    if not os.path.exists('data/stress_dataset.csv'):
        issues.append("Training data not found")
    
    return issues


def display_banner():
    """
    Display application banner
    """
    banner = """
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║          🏥 AI HEALTH CHATBOT                                    ║
║                                                                   ║
║          Stress & Lifestyle Disease Analyzer                     ║
║          with Preventive Health Guidance                         ║
║                                                                   ║
║          Powered by: NLP • Machine Learning • Deep Learning      ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def main():
    """
    Main application function
    """
    display_banner()
    
    # Check requirements
    print("\n🔍 Checking system requirements...\n")
    issues = check_requirements()
    
    if issues:
        print("❌ The following issues were found:\n")
        for issue in issues:
            print(f"   • {issue}")
        print("\n" + "="*70)
        print("\n📝 To fix these issues, please run:")
        print("   python train_models.py")
        print("\n" + "="*70 + "\n")
        sys.exit(1)
    
    print("✅ All requirements met!\n")
    
    # Display model selection
    print("="*70)
    print("SELECT MODEL TYPE:")
    print("="*70)
    print("\n1. Logistic Regression (Fast, Recommended)")
    print("2. Decision Tree")
    print("3. Random Forest (Best Accuracy)")
    print("4. Deep Learning Neural Network (If trained)")
    
    while True:
        choice = input("\nSelect model (1-4) [default: 1]: ").strip()
        
        if not choice:
            choice = '1'
        
        if choice == '1':
            model_type = 'logistic'
            use_dl = False
            break
        elif choice == '2':
            model_type = 'decision_tree'
            use_dl = False
            break
        elif choice == '3':
            model_type = 'random_forest'
            use_dl = False
            break
        elif choice == '4':
            if os.path.exists('models/deep_learning/deep_learning_model.h5'):
                model_type = 'logistic'  # Fallback, won't be used
                use_dl = True
                break
            else:
                print("⚠️  Deep learning model not found. Please train it first.")
                print("   Run: python train_models.py")
                continue
        else:
            print("⚠️  Invalid choice. Please select 1-4.")
    
    print("\n" + "="*70 + "\n")
    
    # Initialize and run chatbot
    try:
        chatbot = HealthChatbot(model_type=model_type, use_deep_learning=use_dl)
        chatbot.interactive_mode()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        print("\nIf this error persists, please retrain the models:")
        print("   python train_models.py")


if __name__ == "__main__":
    main()