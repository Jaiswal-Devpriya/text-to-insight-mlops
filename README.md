Text-to-Insight Dashboard Narrator
A Streamlit-powered tool to auto-generate human-readable summaries from uploaded CSV, PDF, or DOCX files using data profiling and the BART summarization model from Hugging Face.

Project Overview
The Text-to-Insight Dashboard Narrator enables users to quickly understand both structured and unstructured data by combining:

Automated data profiling for CSV files using ydata-profiling

Text extraction from PDF and DOCX files

Natural language summarization using Hugging Face’s facebook/bart-large-cnn model

A simple and clean web interface built with Streamlit

Features
Upload and analyze CSV, PDF, or DOCX files

Generate data profiling reports using ydata-profiling

Extract text from PDF and DOCX using PyMuPDF and python-docx

Summarize datasets and documents using Hugging Face’s BART model

View structured data previews, profiling output, and AI-generated summaries in one place

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
git clone https://github.com/Jaiswal-Devpriya/text-to-insight-mlops.git
cd text-to-insight-mlops
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the app
bash
Copy
Edit
streamlit run app/main.py
File Structure
bash
Copy
Edit
text-to-insight-mlops/
│
├── app/
│   └── main.py                # Streamlit UI and logic
│
├── summarizer/
│   └── summarizer.py          # Text summarization using BART
│
├── utils/
│   └── data_utils.py          # Data profiling and file text extraction
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
Example Use Case
CSV: Upload a sales dataset. The app will:

Show a data preview

Generate a data profile

Use BART to summarize column structure and value patterns

PDF/DOCX: Upload a document. The app will:

Extract the text content

Summarize the content in natural language

Limitations
Summarization model has a token limit (~1024 tokens); long input is split into chunks

Current version supports only CSV, PDF, and DOCX files

Internet is required to load the BART model if not cached

Future Improvements
Add support for Excel files

Integrate OpenAI or LangChain for flexible LLM options

Enable follow-up Q&A over uploaded data

Improve summarization control (e.g., tone, length, chunk strategy)

Contact
Devpriya Jaiswal
Email: jdevpriya2001@gmail.com
LinkedIn: linkedin.com/in/devpriya-jaiswal
