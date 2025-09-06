from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def nl_to_sql(question: str, table: str = "sales") -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a data assistant. Convert user questions into **only valid SQLite SQL queries**. "
                    "Do not explain, just return the SQL. "
                    f"The main table is '{table}', with columns: product, region, revenue, date."
                ),
            },
            {"role": "user", "content": question},
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()
