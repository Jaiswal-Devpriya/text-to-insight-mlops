# app/main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from summarizer.summarizer import generate_summary
from utils.data_utils import (
    generate_profile_report,
    extract_text_from_pdf,
    extract_text_from_docx,
)

st.set_page_config(page_title="Text-to-Insight Dashboard Narrator", layout="wide")

st.title("📊 Text-to-Insight Dashboard Narrator")

uploaded_file = st.file_uploader("Upload your file (CSV, PDF, DOCX)", type=["csv", "pdf", "docx"])

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1]

    if file_type == "csv":
        df = pd.read_csv(uploaded_file)
        st.subheader("📄 Preview of your data")
        st.dataframe(df)

        st.subheader("🧠 Data Profile Summary")
        profile_html = generate_profile_report(df)
        st.components.v1.html(profile_html, height=500, scrolling=True)

        st.subheader("📃 GPT Insight Summary")
        summary = generate_summary(df)
        st.write(summary)

    elif file_type == "pdf":
        text = extract_text_from_pdf(uploaded_file)
        st.subheader("📃 Extracted Text")
        st.write(text[:1000] + "..." if len(text) > 1000 else text)

        st.subheader("🧠 GPT Insight Summary")
        summary = generate_summary(text, is_text=True)
        st.write(summary)

    elif file_type == "docx":
        text = extract_text_from_docx(uploaded_file)
        st.subheader("📃 Extracted Text")
        st.write(text[:1000] + "..." if len(text) > 1000 else text)

        st.subheader("🧠 GPT Insight Summary")
        summary = generate_summary(text, is_text=True)
        st.write(summary)
