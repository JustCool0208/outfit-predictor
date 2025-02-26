import joblib
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

# Sample dataset: [Temperature (°C), Humidity (%), Weather Condition]
X = np.array([
    [5, 80, "Rainy"],
    [15, 60, "Cloudy"],  # Cool & Cloudy
    [25, 50, "Sunny"],  # Warm & Sunny
    [35, 40, "Sunny"],  # Hot & Sunny
    [10, 90, "Rainy"],  # Very Cold & Rainy
    [20, 70, "Cloudy"],  # Mild & Cloudy
])

# Encode the categorical feature "Weather Condition"
label_encoder = LabelEncoder()
X[:, 2] = label_encoder.fit_transform(X[:, 2])

# Labels: Outfit recommendations
y = np.array([
    "Wear a thick jacket and raincoat",
    "Wear a sweater",
    "Wear a t-shirt and jeans",
    "Wear shorts and a t-shirt",
    "Wear a winter coat and boots",
    "Wear a light jacket"
])

# Encode the labels
y_label_encoder = LabelEncoder()
y_encoded = y_label_encoder.fit_transform(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded)
# , test_size=0.2, random_state=42
# Train Decision Tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Print the model score
# score = model.score(X_test, y_test)
# print(f"Model score: {score}")

# Debugging: Print predictions and actual labels
# predictions = model.predict(X_test)
# print(f"Predictions: {predictions}")
# print(f"Actual labels: {y_test}")

# Save the model and the label encoders
joblib.dump(model, "outfit_recommender.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
joblib.dump(y_label_encoder, "y_label_encoder.pkl")
print("Model and label encoders trained and saved successfully!")

