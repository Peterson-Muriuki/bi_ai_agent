import streamlit as st
import pandas as pd

def plot_numeric_data(df: pd.DataFrame):
    numeric_cols = df.select_dtypes(include="number").columns
    if len(numeric_cols) == 0:
        return
    for col in numeric_cols:
        st.line_chart(df[col])
