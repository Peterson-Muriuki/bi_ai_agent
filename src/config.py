from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/sales.db")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
