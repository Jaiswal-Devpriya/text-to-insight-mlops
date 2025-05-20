import pandas_profiling
from ydata_profiling import ProfileReport

def generate_profile_report(df):
    profile = ProfileReport(df, title="Data Profile Report", minimal=True)
    return profile.to_html()
