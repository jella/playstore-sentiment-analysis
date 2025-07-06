import joblib
from sklearn.metrics import accuracy_score

def test_model_accuracy():
    model = joblib.load("backend/model/sentiment_model.pkl")

    # Example mini validation set
    X_test = [
        "Terrible app, full of bugs",
        "Absolutely amazing experience",
        "I didn’t like it at all",
        "Highly recommended, great service",
        "Worst app I've used",
        "Love it, works perfectly"
    ]
    y_test = [0, 1, 0, 1, 0, 1]  # Expected sentiments

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    assert acc >= 0.80, f"Model accuracy too low: {acc}"
