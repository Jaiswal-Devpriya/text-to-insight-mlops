import pandas_profiling
from ydata_profiling import ProfileReport
import fitz  # PyMuPDF
import docx
def generate_profile_report(df):
    profile = ProfileReport(df, title="Data Profile Report", minimal=True)
    return profile.to_html()
# utils/data_utils.py



def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(uploaded_file):
    doc = docx.Document(uploaded_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text
