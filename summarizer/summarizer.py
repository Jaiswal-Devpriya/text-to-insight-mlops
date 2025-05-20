from transformers import pipeline
import pandas as pd
# Load Hugging Face summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(input_data, is_text=False) -> str:
    if is_text:
        input_text = input_data
    else:
        input_text = f"""Columns: {', '.join(input_data.columns)}
        Sample rows: {input_data.head(3).to_string(index=False)}"""

    try:
        # Hugging Face models have a token limit (~1024 tokens for this one)
        chunks = [input_text[i:i+1000] for i in range(0, len(input_text), 1000)]
        summaries = [summarizer(chunk, max_length=200, min_length=50, do_sample=False)[0]['summary_text'] for chunk in chunks]
        return "\n\n".join(summaries)
    except Exception as e:
        return f"Error generating summary: {str(e)}"
