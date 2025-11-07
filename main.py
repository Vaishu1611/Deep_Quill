from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from preprocess import preprocess_text, readability_metrics, tone_analysis
from model import predict_style

app = FastAPI(title="DeepQuill - Writing Style & Readability Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(input: TextInput):
    cleaned = preprocess_text(input.text)
    style = predict_style(cleaned)
    readability = readability_metrics(input.text)
    tone = tone_analysis(input.text)

    return {
        "style": style,
        "readability": readability,
        "tone": tone
    }

@app.get("/")
def root():
    return {"message": "DeepQuill API is running!"}