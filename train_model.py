import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from fetch_data import get_earthquake_data

print("Fetching data...")
df = get_earthquake_data()

# Create risk labels
def risk_label(mag):
    if mag < 4:
        return 0   # Low
    elif mag < 6:
        return 1   # Medium
    else:
        return 2   # High

df["risk"] = df["magnitude"].apply(risk_label)

X = df[["magnitude", "depth"]]
y = df["risk"]

print("Training model...")
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("Model saved as model.pkl ✅")