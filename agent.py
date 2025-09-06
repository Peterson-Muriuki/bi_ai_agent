from groq import Groq
import os

# Initialize Groq client with API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def nl_to_sql(question: str, table: str = "sales") -> str:
    """
    Converts a natural language question into SQL for a simple SQLite table.
    This version calculates total revenue for products/regions if applicable.
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # updated Groq model
        messages=[
            {"role": "system", "content": "You are a data assistant. Convert user questions into SQL queries for SQLite. Only output SQL, no explanations."},
            {"role": "user", "content": f"Table: {table}. Columns: product, region, revenue, date. Question: {question}"}
        ],
        temperature=0,
    )

    # return the SQL string
    return response.choices[0].message.content.strip()
