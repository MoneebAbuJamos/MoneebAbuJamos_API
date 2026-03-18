import joblib

MODEL_PATH = "app/models/sentiment_model.pkl"

model = joblib.load(MODEL_PATH)


def predict_sentiment(text: str):

    prediction = model.predict([text])[0]

    if prediction == 1:
        return "positive"
    else:
        return "negative"


def get_model_info():

    return {
        "model": "Logistic Regression",
        "vectorizer": "TF-IDF",
        "dataset_size": 3000,
        "accuracy": 0.83
    }