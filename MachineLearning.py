# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import os

# From a CSV file
df = pd.read_csv('cereal.csv')
print(df)
df.columns 
print(df.columns)

# Create a binary target variable 'high_rating' based on the rating column
df['high_rating'] = df['rating'].apply(lambda x: 1 if x > 50 else 0)

# Drop the original rating column (as it is now used to create the target variable)
X = df.drop(['name','mfr', 'type', 'high_rating'], axis=1)
y = df['high_rating']
# Step 4: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train a Machine Learning Model
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Scale the features
model = LogisticRegression(max_iter=300)
model.fit(X_train, y_train)

# Step 6: Make Predictions and Evaluate the Model
y_pred = model.predict(X_test)

# Evaluate the model
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

