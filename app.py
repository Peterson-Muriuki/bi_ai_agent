import streamlit as st
from src.agent import nl_to_sql
from src.db import run_query
from src.visualizer import plot_numeric_data

st.title("📊 Business Intelligence AI Agent")

user_query = st.text_input("Ask a business question:")

if user_query:
    sql = nl_to_sql(user_query)
    st.write(f"Generated SQL: `{sql}`")

    df = run_query(sql)

    if "error" in df.columns:
        st.error(df["error"][0])
    else:
        st.dataframe(df)
        plot_numeric_data(df)
