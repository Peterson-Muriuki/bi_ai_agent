import pandas as pd
from sqlalchemy import create_engine, text

DB_PATH = "sqlite:///data/sales.db"
engine = create_engine(DB_PATH)

def run_query(query: str) -> pd.DataFrame:
    try:
        with engine.connect() as conn:
            return pd.read_sql(text(query), conn)
    except Exception as e:
        return pd.DataFrame({"error": [str(e)]})
