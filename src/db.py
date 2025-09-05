import pandas as pd
from sqlalchemy import create_engine
from src.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def run_query(sql):
    try:
        df = pd.read_sql(sql, engine)
        return df
    except Exception as e:
        return pd.DataFrame({"error": [str(e)]})
