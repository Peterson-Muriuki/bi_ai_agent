import sqlite3, os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Connect to SQLite DB
conn = sqlite3.connect("data/sales.db")
c = conn.cursor()

# Drop old table if exists
c.execute("DROP TABLE IF EXISTS sales")

# Create sales table
c.execute("""
CREATE TABLE sales (
  product TEXT,
  region  TEXT,
  revenue REAL,
  date    TEXT
)
""")

# Insert demo rows
rows = [
  ("ProductA","Nairobi",1200,"2025-01-10"),
  ("ProductB","Mombasa", 900,"2025-02-15"),
  ("ProductC","Nairobi",3000,"2025-03-12"),
  ("ProductA","Nairobi",1800,"2025-04-11"),
  ("ProductC","Nakuru", 700,"2025-04-20"),
]
c.executemany("INSERT INTO sales VALUES (?,?,?,?)", rows)

conn.commit()
conn.close()
print("✅ Demo SQLite DB created at data/sales.db")
