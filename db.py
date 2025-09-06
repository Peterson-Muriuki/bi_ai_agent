import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from src.config import DATABASE_URL

_engine = None

def get_engine():
    global _engine
    if _engine is None:
        # Ensure SQLite folder exists if using sqlite:///data/sales.db
        if DATABASE_URL.startswith("sqlite:///"):
            folder = DATABASE_URL.replace("sqlite:///", "")
            folder = os.path.dirname(folder)
            if folder and not os.path.exists(folder):
                os.makedirs(folder, exist_ok=True)
        _engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    return _engine

def run_query(sql: str) -> pd.DataFrame:
    try:
        eng = get_engine()
        with eng.connect() as conn:
            df = pd.read_sql(text(sql), conn)
        return df
    except SQLAlchemyError as e:
        return pd.DataFrame({"error": [str(e.__cause__ or e)]})
    except Exception as e:
        return pd.DataFrame({"error": [str(e)]})
