import sqlite3

connection = sqlite3.connect(
    "experiments/sql/databases/commerceops.db"
)

cursor = connection.cursor()

cursor.execute("""
SELECT * FROM inventory
""")

rows = cursor.fetchall()

print(rows)

connection.close()