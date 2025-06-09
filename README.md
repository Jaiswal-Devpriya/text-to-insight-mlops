Text-to-Insight Dashboard Narrator
A Streamlit tool that generates natural language insights from structured data or documents using pandas profiling and Hugging Face's BART summarization model.

Project Overview
The Text-to-Insight Dashboard Narrator is a lightweight application that helps users quickly understand datasets and documents. It accepts CSV, PDF, or DOCX files, extracts or profiles the content, and summarizes the key information using an LLM-based approach via the facebook/bart-large-cnn model.

Features
Upload CSV, PDF, or DOCX files

Generate a data profiling report for tabular data using ydata-profiling

Extract raw text from PDF and DOCX using PyMuPDF and python-docx

Summarize data and documents using Hugging Face’s BART model

Interactive and user-friendly Streamlit dashboard

Tech Stack
Python

Streamlit

pandas, ydata-profiling

Hugging Face Transformers (facebook/bart-large-cnn)

PyMuPDF (fitz), python-docx

Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/text-to-insight-narrator.git
cd text-to-insight-narrator
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Streamlit app
bash
Copy
Edit
streamlit run app/main.py
File Structure
bash
Copy
Edit
text-to-insight-narrator/
│
├── app/
│   └── main.py                  # Streamlit frontend logic
│
├── summarizer/
│   └── summarizer.py            # Summarization logic using BART
│
├── utils/
│   └── data_utils.py            # Data profiling and text extraction
│
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation
Example Use Case
Upload a CSV of sales data:

The app previews the data

Generates a profile using ydata-profiling

Summarizes column types, missing values, and key patterns using the summarization model

Upload a PDF or DOCX:

The app extracts the text content

The summarizer generates a condensed narrative of the file’s contents

Limitations
Hugging Face models have a token limit (~1024 tokens); longer text is chunked

Currently supports only CSV, PDF, and DOCX

Internet connection required to download the BART model if not cached

Future Improvements
Support for Excel and other file types

Integration with OpenAI or LangChain for advanced LLM capabilities

Ability to ask questions over the uploaded data/documents

Improved chunk handling and summarization controls

Contact
Devpriya Jaiswal
Email: jdevpriya2001@gmail.com
LinkedIn: linkedin.com/in/devpriya-jaiswal

