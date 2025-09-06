import streamlit as st
from src.agent import nl_to_sql
from src.db import run_query
from src.visualizer import plot_numeric_data
from groq import Groq

# --- Initialize Groq client safely ---
try:
    api_key = st.secrets["GROQ_API_KEY"]
except KeyError:
    api_key = None

if api_key:
    client = Groq(api_key=api_key)
else:
    client = None
    st.warning(
        "⚠️ Groq API key is missing. Please add it to Streamlit secrets for the AI assistant to work."
    )

# --- Streamlit page setup ---
st.set_page_config(page_title="Business Intelligence AI Agent", page_icon="📊", layout="wide")
st.title("📊 Business Intelligence AI Agent")
st.caption("Ask questions like: Top 5 products this quarter, Show revenue trends in Nairobi, Total revenue by region.")

# --- User input ---
user_query = st.text_input("Ask a business question:")
default_table = st.text_input("Table name", value="sales")

if user_query:
    if client is None:
        st.error("AI assistant unavailable. Groq API key is not set.")
    else:
        # Convert natural language question to SQL
        sql = nl_to_sql(user_query, table=default_table)

        with st.expander("Generated SQL", expanded=False):
            st.code(sql, language="sql")

        # Run SQL query
        df = run_query(sql)

        if "error" in df.columns:
            st.error(df["error"][0])
        else:
            # Show dataframe
            st.dataframe(df, use_container_width=True)

            # Automatically plot numeric columns if they exist
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
            if numeric_cols.any():
                st.subheader("📈 Visualizations")
                plot_numeric_data(df)
