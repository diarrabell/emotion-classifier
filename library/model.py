"""
This file contains the main function for the code.
It uses the Emotion English DistilRoBERTa-base mode, which classifies text into one of 6 different emotions.
"""
from transformers import pipeline

def classify(text):
    #download sentiment analysis model
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

    #return results
    results = classifier(text)
    return results

