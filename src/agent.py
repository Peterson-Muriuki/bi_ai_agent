import openai
from src.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def nl_to_sql(user_query, table="sales"):
    prompt = f"""
    You are a SQL assistant. Convert the user question into a SQL query.
    Table: {table} has columns (product, region, revenue, date).
    User: {user_query}
    SQL:
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0
    )
    sql = response.choices[0].text.strip()
    return sql
