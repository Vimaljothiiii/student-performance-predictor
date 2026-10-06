import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("dataset.csv")

X = data[["study_hours", "attendance", "previous_score", "assignment_score"]]
y = data["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Model Accuracy:", accuracy)

with open("backend/model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")
