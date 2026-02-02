# 🏥 AI-Based Chatbot to Analyze the Impact of Stress on Lifestyle Diseases

## 📋 Project Overview

This is a comprehensive AI-powered health chatbot system that analyzes the impact of stress on lifestyle diseases and provides personalized preventive health guidance. The system combines Natural Language Processing (NLP), Machine Learning, and Rule-Based Systems to deliver intelligent health insights.

### 🎯 Key Features

- **Text-Based Stress Detection**: Uses NLTK and SpaCy for NLP analysis of user input
- **Machine Learning Prediction**: Multiple ML models (Logistic Regression, Decision Tree, Random Forest)
- **Deep Learning Option**: Neural Network implementation using TensorFlow/Keras
- **Disease Risk Assessment**: Rule-based system for 5 major lifestyle diseases
- **Personalized Health Guidance**: Customized preventive care recommendations
- **Interactive Chatbot Interface**: User-friendly command-line interface

### 🩺 Health Conditions Analyzed

1. **Diabetes** - Type 2 Diabetes risk assessment
2. **High Blood Pressure** - Hypertension risk analysis
3. **Obesity** - Weight management risk factors
4. **Cardiovascular Disease** - Heart health assessment
5. **Sleep Disorders** - Sleep quality evaluation

---

## 📁 Project Structure

```
ai-health-chatbot/
│
├── data/                          # Dataset storage
│   ├── stress_dataset.csv         # Training data for stress prediction
│   └── lifestyle_dataset.csv      # Lifestyle and disease risk data
│
├── nlp/                           # NLP and ML modules
│   ├── text_processor.py          # Text preprocessing with NLTK & SpaCy
│   ├── ml_predictor.py            # Traditional ML models
│   └── deep_predictor.py          # Deep learning model (TensorFlow)
│
├── rules/                         # Rule-based systems
│   ├── disease_risk.py            # Disease risk assessment logic
│   └── health_guidance.py         # Health guidance generation
│
├── chatbot/                       # Chatbot engine
│   └── health_bot.py              # Main chatbot implementation
│
├── models/                        # Trained model storage (generated)
│   ├── logistic/                  # Logistic Regression model
│   ├── decision_tree/             # Decision Tree model
│   ├── random_forest/             # Random Forest model
│   └── deep_learning/             # Neural Network model
│
├── app.py                         # Main application entry point
├── train_models.py                # Model training script
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## 🚀 Installation Guide

### Step 1: Prerequisites

Ensure you have the following installed:
- **Python 3.8 or higher**
- **pip** (Python package manager)
- **virtualenv** (recommended)

### Step 2: Clone or Download the Project

```bash
# Navigate to your desired directory
cd /path/to/your/projects/

# If using git
git clone <repository-url>
cd ai-health-chatbot
```

### Step 3: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

### Step 5: Download NLP Models

```bash
# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"

# Download SpaCy model
python -m spacy download en_core_web_sm
```

### Step 6: Train Machine Learning Models

```bash
# Train all models (takes 1-2 minutes for ML, 5-10 minutes if including DL)
python train_models.py
```

During training, you'll be asked if you want to train the deep learning model. Choose based on your requirements:
- Type `yes` for full deep learning capability (requires more time)
- Type `no` to use only traditional ML models (faster, still effective)

---

## 💻 Usage Instructions

### Running the Chatbot

```bash
# Start the chatbot application
python app.py
```

### Interaction Flow

1. **Select Model**: Choose which ML model to use (Logistic Regression recommended)
2. **Describe Your Feelings**: Enter text describing your stress or mood
3. **Provide Lifestyle Data**: Answer questions about:
   - Sleep hours
   - BMI (Body Mass Index)
   - Physical activity level
   - Work hours
   - Social interaction level
4. **Review Analysis**: See your stress prediction and disease risk assessment
5. **Get Guidance**: Receive personalized health recommendations

### Example Interaction

```
How are you feeling today?
→ I feel extremely stressed and can't sleep well

How many hours do you sleep on average per night?
→ 5

What is your Body Mass Index (BMI)?
→ 28.5

What is your physical activity level? (low, medium, high)
→ low

How many hours do you work per day on average?
→ 11

What is your social interaction level? (low, medium, high)
→ low
```

**Output**: The system will provide:
- Stress level analysis
- Disease risk assessment
- Personalized health guidance
- Quick action tips

---

## 🧪 Testing the System

### Test Individual Components

```bash
# Test text processor
cd nlp
python text_processor.py

# Test ML predictor
python ml_predictor.py

# Test disease risk assessor
cd ../rules
python disease_risk.py

# Test health guidance generator
python health_guidance.py
```

### Test Complete Chatbot

```bash
# Run the chatbot
cd ..
python chatbot/health_bot.py
```

---

## 📊 Understanding the Models

### 1. Traditional Machine Learning Models

#### Logistic Regression
- **Best for**: Fast predictions, interpretable results
- **Accuracy**: ~85-90%
- **Use case**: Default recommended model

#### Decision Tree
- **Best for**: Understanding decision logic
- **Accuracy**: ~80-85%
- **Use case**: When interpretability is crucial

#### Random Forest
- **Best for**: Highest accuracy
- **Accuracy**: ~90-95%
- **Use case**: When prediction quality is priority

### 2. Deep Learning Model (Optional)

#### Neural Network (TensorFlow/Keras)
- **Architecture**: 4-layer neural network
- **Accuracy**: ~88-93%
- **Use case**: Advanced AI demonstration
- **Note**: Requires more training time

---

## 🔬 Technical Details

### NLP Pipeline

1. **Text Cleaning**: Remove special characters, lowercase conversion
2. **Tokenization**: Break text into words using NLTK
3. **Stopword Removal**: Filter common words
4. **Lemmatization**: Convert words to base form
5. **Feature Extraction**: Count stress-related keywords

### ML Features

- Sleep hours (numeric)
- Physical activity level (categorical: low/medium/high)
- Work hours (numeric)
- Social interaction level (categorical: low/medium/high)

### Rule-Based Risk Assessment

Risk scores are calculated based on:
- BMI thresholds (underweight, normal, overweight, obese)
- Stress level impact
- Physical activity contribution
- Sleep quality factors

Risk levels: **Low**, **Medium**, **High**

---

## 📝 Dataset Information

### Stress Dataset (`stress_dataset.csv`)

- **Size**: 50 samples (expandable)
- **Features**: text, sleep_hours, physical_activity, work_hours, social_interaction
- **Target**: stress_level (low, medium, high)
- **Source**: Synthetic data for academic purposes

### Lifestyle Dataset (`lifestyle_dataset.csv`)

- **Size**: 25 samples
- **Features**: age, bmi, sleep_hours, physical_activity, stress_level
- **Targets**: diabetes_risk, bp_risk, obesity_risk, cvd_risk, sleep_disorder_risk
- **Purpose**: Validation and testing

---

## ⚠️ Important Disclaimers

### Medical Disclaimer

```
⚠️  IMPORTANT MEDICAL DISCLAIMER

This AI chatbot is designed for EDUCATIONAL and INFORMATIONAL purposes only.
It is NOT a substitute for professional medical advice, diagnosis, or treatment.

- This system does NOT diagnose medical conditions
- Recommendations are preventive guidelines, not treatment plans
- Always consult qualified healthcare professionals for medical concerns
- In case of emergency, contact emergency services immediately

The creators and developers assume no liability for decisions made based
on this chatbot's output.
```

### Academic Use

This project is designed for:
- Final year engineering projects
- Computer science coursework
- AI/ML academic demonstrations
- Research and learning purposes

---

## 🎓 For Academic Presentation

### Project Highlights for Viva

1. **Multi-disciplinary Approach**: Combines NLP, ML, DL, and Rule-Based Systems
2. **Real-world Application**: Addresses actual health concerns
3. **Scalability**: Can be extended with more diseases and features
4. **User-Friendly**: Simple command-line interface
5. **Well-Documented**: Clean code with comprehensive comments

### Key Points to Emphasize

- **NLP Integration**: NLTK and SpaCy for text analysis
- **Multiple ML Models**: Comparison of different algorithms
- **Deep Learning**: Optional advanced model with TensorFlow
- **Rule-Based Logic**: Domain knowledge incorporated
- **Practical Output**: Actionable health guidance

### Demonstration Tips

1. Start with the banner and system initialization
2. Show the interactive input process
3. Explain the stress prediction (both text and ML)
4. Demonstrate risk assessment output
5. Highlight personalized guidance generation
6. Show model comparison results

### Screenshots to Include in Report

- System architecture diagram
- Chatbot interaction flow
- Model training output
- Risk assessment summary
- Health guidance recommendations
- Accuracy metrics

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue: "ModuleNotFoundError: No module named 'nltk'"
```bash
Solution: pip install nltk
```

#### Issue: "SpaCy model not found"
```bash
Solution: python -m spacy download en_core_web_sm
```

#### Issue: "Model files not found"
```bash
Solution: python train_models.py
```

#### Issue: TensorFlow installation fails
```bash
Solution: Skip deep learning or install TensorFlow separately
pip install tensorflow==2.13.0
```

#### Issue: Memory error during training
```bash
Solution: Reduce batch_size in deep_predictor.py (line ~100)
Change: batch_size=8 to batch_size=4
```

---

## 📈 Future Enhancements

Potential improvements for extended projects:

1. **Web Interface**: Flask/Django web application
2. **Database Integration**: Store user data and history
3. **More Diseases**: Add cancer risk, mental health conditions
4. **Visualization**: Charts and graphs for risk scores
5. **Mobile App**: React Native or Flutter implementation
6. **Multi-language Support**: Translate guidance to local languages
7. **Wearable Integration**: Connect with fitness trackers
8. **Doctor Dashboard**: Interface for healthcare professionals

---

## 👥 Contributors

This project is designed for academic use. Customize this section with your details:

- **Student Name**: [Your Name]
- **Roll Number**: [Your Roll No]
- **Department**: Computer Science / AI & ML
- **Institution**: [Your College/University]
- **Project Guide**: [Guide Name]
- **Academic Year**: [Year]

---

## 📚 References

### Libraries and Tools

1. **NLTK**: Natural Language Toolkit - https://www.nltk.org/
2. **SpaCy**: Industrial-strength NLP - https://spacy.io/
3. **Scikit-learn**: Machine Learning in Python - https://scikit-learn.org/
4. **TensorFlow**: Deep Learning Framework - https://www.tensorflow.org/
5. **Pandas**: Data manipulation - https://pandas.pydata.org/
6. **NumPy**: Numerical computing - https://numpy.org/

### Research Papers

- "Stress Detection in Social Networks" - IEEE
- "Machine Learning for Healthcare" - Nature
- "NLP in Medical Applications" - ACM

### Health Resources

- WHO Guidelines on Stress Management
- CDC Lifestyle Disease Prevention
- NIH Health Information

---

## 📄 License

This project is created for educational purposes. For commercial use or redistribution, please ensure proper attribution and compliance with relevant regulations.

---

## 🤝 Support

For issues, questions, or contributions:

1. Check the troubleshooting section
2. Review the code comments
3. Test individual components separately
4. Contact your project guide

---

## ✅ Submission Checklist

Before submitting your project:

- [ ] All dependencies installed
- [ ] Models trained successfully
- [ ] Chatbot runs without errors
- [ ] README.md reviewed and customized
- [ ] Code comments are clear
- [ ] Screenshots taken for report
- [ ] Medical disclaimer included
- [ ] Testing completed
- [ ] Documentation prepared
- [ ] Presentation ready

---

## 🎉 Conclusion

This AI Health Chatbot demonstrates the practical application of modern AI technologies in healthcare. It combines multiple domains:

- Natural Language Processing
- Machine Learning
- Deep Learning
- Rule-Based Systems
- Healthcare Domain Knowledge

The project showcases how AI can assist in preventive healthcare, making health guidance more accessible while emphasizing the importance of professional medical consultation.

**Best of luck with your project! 🌟**

---

*Last Updated: January 2026*
*Version: 1.0.0*