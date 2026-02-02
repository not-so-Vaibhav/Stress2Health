import pandas as pd
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("stress_text.csv")

# Text cleaning function
def clean_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))

    tokens = [
        w for w in tokens
        if w.isalpha() and w not in stop_words
    ]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(w) for w in tokens]

    return " ".join(tokens)

df["clean_text"] = df["text"].apply(clean_text)

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["clean_text"])
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict new text
user_text = "I feel anxious and stressed due to work pressure"
cleaned = clean_text(user_text)
vector = vectorizer.transform([cleaned])

prediction = model.predict(vector)
print("Predicted Stress Level:", prediction[0])
