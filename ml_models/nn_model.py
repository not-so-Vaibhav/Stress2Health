import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Load dataset
df = pd.read_csv("data/stress_dataset.csv")

# Safety check
print("Dataset shape:", df.shape)
print(df.head())

# Features & target (ALREADY NUMERIC)
X = df[["sleep_hours", "work_hours", "physical_activity"]]
y = df["stress_level"]

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Neural Network
model = Sequential([
    Input(shape=(X_train.shape[1],)),
    Dense(16, activation="relu"),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train
model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=4,
    validation_data=(X_test, y_test)
)

# Evaluate
loss, acc = model.evaluate(X_test, y_test)
print("Accuracy:", acc)

# Predict new user
sample = scaler.transform([[6, 9, 1]])
prob = model.predict(sample)[0][0]

print("Stress Probability:", round(prob, 2))
print("Stress Level:", "High" if prob > 0.5 else "Low")
