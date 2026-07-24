import sqlite3

connection = sqlite3.connect(
    "experiments/sql/databases/commerceops.db"
)

cursor = connection.cursor()

cursor.execute("""
SELECT SUM(quantity)
FROM inventory
WHERE price > 900
""")

rows = cursor.fetchall()

print(rows)

connection.close()