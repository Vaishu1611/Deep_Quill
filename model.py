import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

data = [
    ("The government has announced new policies to improve trade.", "Formal"),
    ("Once upon a time, in a faraway land, there lived a king.", "Narrative"),
    ("The phone features an advanced camera and fast processor.", "Informative"),
    ("The soft breeze carried the scent of roses through the garden.", "Descriptive"),
    ("Buy one, get one free! Don’t miss this amazing offer!", "Persuasive")
]

texts, labels = zip(*data)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)

model = LinearSVC()
model.fit(X, labels)

joblib.dump((model, vectorizer), "style_model.pkl")

def predict_style(text: str):
    model, vectorizer = joblib.load("style_model.pkl")
    X = vectorizer.transform([text])
    return model.predict(X)[0]