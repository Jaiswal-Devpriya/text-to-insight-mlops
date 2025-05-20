import openai
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(df: pd.DataFrame) -> str:
    prompt = f"""You are a data analyst. Based on this dataset summary, generate an executive-level summary:
    
    Columns: {', '.join(df.columns)}
    Sample rows: {df.head(3).to_string(index=False)}

    Keep it concise and insight-driven.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating summary: {str(e)}"
