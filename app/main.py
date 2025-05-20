import streamlit as st
import pandas as pd
from summarizer.summarizer import generate_summary
from utils.data_utils import generate_profile_report

st.set_page_config(page_title="Text-to-Insight Dashboard Narrator", layout="wide")

st.title("📊 Text-to-Insight Dashboard Narrator")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of your data")
    st.dataframe(df)

    st.subheader("Generated Profile Summary")
    profile_html = generate_profile_report(df)

    st.components.v1.html(profile_html, height=500, scrolling=True)

    st.subheader("📃 Text Summary using GPT")
    summary = generate_summary(df)
    st.write(summary)
