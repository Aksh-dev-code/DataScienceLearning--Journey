import streamlit as st
import pandas as pd

# First file uploader
file1 = st.file_uploader("Upload a CSV file", type=["csv"], key="file1")

# Another file uploader
file2 = st.file_uploader("Upload another CSV file", type=["csv"], key="file2")

if file1 is not None:
    df1 = pd.read_csv(file1)
    st.write("First CSV", df1)

if file2 is not None:
    df2 = pd.read_csv(file2)
    st.write("Second CSV", df2)
