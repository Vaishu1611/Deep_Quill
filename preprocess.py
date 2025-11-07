import spacy
import textstat
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text: str):
    """Basic text cleaning and lemmatization"""
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc 
              if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def readability_metrics(text: str):
    """Compute readability and lexical metrics"""
    return {
        "flesch_reading_ease": round(textstat.flesch_reading_ease(text), 2),
        "flesch_kincaid_grade": round(textstat.flesch_kincaid_grade(text), 2),
        "avg_sentence_length": round(textstat.avg_sentence_length(text), 2),
        "lexical_diversity": round(len(set(text.split())) / len(text.split()), 2)
    }

def tone_analysis(text: str):
    """Compute sentiment polarity and subjectivity"""
    blob = TextBlob(text)
    return {
        "polarity": round(blob.sentiment.polarity, 2),
        "subjectivity": round(blob.sentiment.subjectivity, 2)
    }