# Text-to-Insight Dashboard Narrator

**A Streamlit-powered tool to auto-generate human-readable summaries from uploaded CSV, PDF, or DOCX files using data profiling and the BART summarization model from Hugging Face.**

---

## **Project Overview**

The Text-to-Insight Dashboard Narrator enables users to quickly understand both structured and unstructured data by combining:

- Automated data profiling for CSV files using `ydata-profiling`  
- Text extraction from PDF and DOCX files  
- Natural language summarization using Hugging Face’s `facebook/bart-large-cnn` model  
- A simple and clean web interface built with Streamlit

---

## **Features**

- Upload and analyze CSV, PDF, or DOCX files  
- Generate data profiling reports using `ydata-profiling`  
- Extract text from PDF and DOCX using PyMuPDF and `python-docx`  
- Summarize datasets and documents using Hugging Face’s BART model  
- View structured data previews, profiling output, and AI-generated summaries in one place

---

## **Tech Stack**

- Python  
- Streamlit  
- pandas, ydata-profiling  
- Hugging Face Transformers (`facebook/bart-large-cnn`)  
- PyMuPDF (`fitz`), `python-docx`

---

## **Getting Started**

### 1. Clone the repository

git clone https://github.com/Jaiswal-Devpriya/text-to-insight-mlops.git
cd text-to-insight-mlops

2. Install dependencies
pip install -r requirements.txt

4. Run the app
streamlit run app/main.py

5.File Structure
text-to-insight-mlops/
│
├── app/
│ └── main.py # Streamlit UI and logic
│
├── summarizer/
│ └── summarizer.py # Text summarization using BART
│
├── utils/
│ └── data_utils.py # Data profiling and file text extraction
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

6.Example Use Case
CSV: Upload a tabular dataset (e.g., sales data). The app will:

Show a data preview

Generate a data profile using ydata-profiling

Summarize structure and patterns using BART

PDF/DOCX: Upload a document. The app will:

Extract raw text

Generate a concise summary of the content

7.Limitations
BART model has a token limit (~1024 tokens); long input is chunked automatically

Currently supports only CSV, PDF, and DOCX formats

Requires internet to load Hugging Face model if not cached locally

8.Future Improvements
Add support for Excel files

Integrate OpenAI API or LangChain for advanced summarization and Q&A

Improve summarization customization (e.g., tone, length control)

Enhance error handling and UI responsiveness

Contact
Devpriya Jaiswal
Email: jdevpriya2001@gmail.com
LinkedIn: https://linkedin.com/in/devpriya-jaiswal
