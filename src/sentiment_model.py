import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

def split_data(X, y, seed=42):
    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=0.15, random_state=seed, stratify=y)

    val_size = 0.15 / 0.85
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=val_size, random_state=seed, stratify=y_train_val)

    return X_train, X_val, X_test, y_train, y_val, y_test

def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X, y, name=""):
    y_pred = model.predict(X)
    print(f"\n--- Evaluación en {name} ---")
    print(f"Accuracy: {accuracy_score(y, y_pred):.4f}")
    print(classification_report(y, y_pred))

def save_model(model, path='models/sentiment_model.pkl'):
    joblib.dump(model, path)
