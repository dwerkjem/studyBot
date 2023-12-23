# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("question-answering", model="timpal0l/mdeberta-v3-base-squad2")
