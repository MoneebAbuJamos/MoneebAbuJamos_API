import os
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


def load_dataset():

    texts = []
    labels = []

    files = [
        "app/data/amazon_cells_labelled.txt",
        "app/data/imdb_labelled.txt",
        "app/data/yelp_labelled.txt"
    ]

    for file in files:
        with open(file, encoding="utf-8") as f:
            for line in f:
                sentence, label = line.strip().split("\t")
                texts.append(sentence)
                labels.append(int(label))

    return texts, labels


texts, labels = load_dataset()


X_train, X_test, y_train, y_test = train_test_split(
    texts,
    labels,
    test_size=0.2,
    random_state=42
)


model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])


model.fit(X_train, y_train)


predictions = model.predict(X_test)

print("\nModel Evaluation:\n")

print("Classification Report:")
print(classification_report(y_test, predictions))

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

os.makedirs("app/models", exist_ok=True)

joblib.dump(model, "app/models/sentiment_model.pkl")

print("\nModel trained and saved successfully!")