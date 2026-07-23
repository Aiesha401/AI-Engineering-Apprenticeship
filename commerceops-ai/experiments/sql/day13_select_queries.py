import sqlite3

connection = sqlite3.connect(
    "experiments/sql/databases/commerceops.db"
)

cursor = connection.cursor()

cursor.execute("""
SELECT product,price
FROM inventory
WHERE price > 900
ORDER BY price DESC
""")

rows = cursor.fetchall()

print(rows)

connection.close()