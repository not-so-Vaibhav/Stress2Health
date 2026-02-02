"""
NLP Text Processor Module
This module handles text cleaning, preprocessing, and feature extraction
using NLTK and SpaCy for stress detection from user messages.
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy

class TextProcessor:
    """
    Text processing class for NLP operations
    """
    
    def __init__(self):
        """
        Initialize NLP tools and download necessary NLTK data
        """
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
        
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet', quiet=True)
        
        # Initialize lemmatizer and stopwords
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
        # Try to load SpaCy model
        try:
            self.nlp = spacy.load('en_core_web_sm')
        except OSError:
            print("SpaCy model not found. Run: python -m spacy download en_core_web_sm")
            self.nlp = None
        
        # Stress-related keywords for feature extraction
        self.stress_keywords = {
            'high_stress': ['anxious', 'stressed', 'overwhelmed', 'panic', 'worried', 
                           'exhausted', 'burnt', 'pressure', 'tense', 'depressed',
                           'anxiet', 'overwhelming', 'burnout', 'chaotic'],
            'low_stress': ['relaxed', 'calm', 'peaceful', 'happy', 'great', 
                          'wonderful', 'balanced', 'content', 'motivated', 'harmony']
        }
    
    def clean_text(self, text):
        """
        Clean text by removing special characters, extra spaces, etc.
        
        Args:
            text (str): Raw input text
            
        Returns:
            str: Cleaned text
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespaces
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def tokenize_text(self, text):
        """
        Tokenize text into words
        
        Args:
            text (str): Input text
            
        Returns:
            list: List of tokens
        """
        return word_tokenize(text)
    
    def remove_stopwords(self, tokens):
        """
        Remove stopwords from token list
        
        Args:
            tokens (list): List of tokens
            
        Returns:
            list: Filtered tokens
        """
        return [token for token in tokens if token not in self.stop_words]
    
    def lemmatize_tokens(self, tokens):
        """
        Lemmatize tokens to their base form
        
        Args:
            tokens (list): List of tokens
            
        Returns:
            list: Lemmatized tokens
        """
        return [self.lemmatizer.lemmatize(token) for token in tokens]
    
    def preprocess_text(self, text):
        """
        Complete preprocessing pipeline
        
        Args:
            text (str): Raw input text
            
        Returns:
            list: Processed tokens
        """
        # Clean text
        cleaned_text = self.clean_text(text)
        
        # Tokenize
        tokens = self.tokenize_text(cleaned_text)
        
        # Remove stopwords
        tokens = self.remove_stopwords(tokens)
        
        # Lemmatize
        tokens = self.lemmatize_tokens(tokens)
        
        return tokens
    
    def extract_stress_features(self, text):
        """
        Extract stress-related features from text
        
        Args:
            text (str): Input text
            
        Returns:
            dict: Feature dictionary
        """
        # Preprocess text
        tokens = self.preprocess_text(text)
        processed_text = ' '.join(tokens)
        
        # Count stress keywords
        high_stress_count = sum(1 for keyword in self.stress_keywords['high_stress'] 
                               if keyword in processed_text)
        low_stress_count = sum(1 for keyword in self.stress_keywords['low_stress'] 
                              if keyword in processed_text)
        
        # SpaCy features (if available)
        sentiment_score = 0
        if self.nlp:
            doc = self.nlp(text)
            # Simple sentiment based on word polarity
            sentiment_score = low_stress_count - high_stress_count
        
        features = {
            'high_stress_keywords': high_stress_count,
            'low_stress_keywords': low_stress_count,
            'word_count': len(tokens),
            'sentiment_score': sentiment_score,
            'processed_text': processed_text
        }
        
        return features
    
    def predict_stress_from_text(self, text):
        """
        Simple rule-based stress prediction from text
        
        Args:
            text (str): Input text
            
        Returns:
            str: Predicted stress level ('low', 'medium', 'high')
        """
        features = self.extract_stress_features(text)
        
        high_count = features['high_stress_keywords']
        low_count = features['low_stress_keywords']
        
        # Simple rule-based classification
        if high_count >= 2 or (high_count > 0 and low_count == 0):
            return 'high'
        elif low_count >= 2 or (low_count > 0 and high_count == 0):
            return 'low'
        else:
            return 'medium'


# Example usage
if __name__ == "__main__":
    processor = TextProcessor()
    
    # Test cases
    test_texts = [
        "I feel extremely stressed and anxious about work",
        "I'm feeling great and relaxed today",
        "Work is okay but manageable"
    ]
    
    for text in test_texts:
        print(f"\nText: {text}")
        features = processor.extract_stress_features(text)
        stress_level = processor.predict_stress_from_text(text)
        print(f"Features: {features}")
        print(f"Predicted Stress Level: {stress_level}")