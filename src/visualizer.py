import matplotlib.pyplot as plt
import streamlit as st

def plot_numeric_data(df):
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_cols) == 0:
        st.info("No numeric data to plot.")
        return

    st.line_chart(df[numeric_cols])
