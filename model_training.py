import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("data/event_data.csv")

# Create variance column
df["variance"] = df["Actual"] - df["Planned"]

# Target variable (1 = over budget, 0 = within budget)
df["over_budget"] = df["variance"].apply(lambda x: 1 if x > 0 else 0)

# Features (inputs for model)
X = df[["Planned", "Actual", "Sponsorship"]]

# Target (output)
y = df["over_budget"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save trained model
pickle.dump(model, open("model/budget_model.pkl", "wb"))

print("Model trained and saved successfully.")