import sqlite3

connection = sqlite3.connect(
    "experiments/sql/databases/commerceops.db"
)

cursor = connection.cursor()

def get_quantity(product):
    cursor.execute("""
    SELECT quantity
    FROM inventory
    WHERE product = ?
    """,(product,))

    row = cursor.fetchone()

    if row:
        return row[0]
    return None

# print(get_quantity("iPhone 16"))

def get_price(product):
    cursor.execute("""
    SELECT price
    FROM inventory
    WHERE product = ?
    """,(product,))

    row = cursor.fetchone()

    if row:
        return row[0]
    return None

print(get_price("MacBook Air"))

cursor.execute("""
PRAGMA table_info(inventory)
""")

# print(cursor.fetchall())

connection.close()