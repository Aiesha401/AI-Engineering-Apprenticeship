import sqlite3

connection = sqlite3.connect(
    "mini_projects/commerceops_agent/commerceops.db",
    check_same_thread=False
)

cursor = connection.cursor()

def get_inventory(product):
    # inventory = {
    #     "iphone 16": 42,
    #     "samsung s24": 18,
    #     "macbook air": 9
    # }

    # return inventory.get(product.lower(), "Product not found")
    cursor.execute("""
    SELECT quantity
    FROM inventory
    WHERE LOWER(product) = LOWER(?)
    """,(product,))

    row = cursor.fetchone()

    if row:
        return row[0]
    return "Product not found"

def get_inventory_report():
    # return{
    #     "iphone 16": 42,
    #     "samsung s24": 18,
    #     "macbook air": 9
    # }
    cursor.execute("""
    SELECT product,quantity
    FROM inventory
    """)

    row = cursor.fetchall()
    report = {}
    for product,quantity in row:
        report[product] = quantity
    return report

def get_total_revenue():
    # return "$12,500"
    cursor.execute("""
    SELECT SUM(quantity*price)
    FROM inventory
    """)
    row = cursor.fetchone()
    if row:
        return f"${row[0]:,.2f}"
    return "$0.00"

def get_top_product():
    # return "iPhone 16"
    cursor.execute("""
    SELECT product
    FROM inventory
    ORDER BY quantity DESC
    LIMIT 1
    """)
    row = cursor.fetchone()
    if row:
        return row[0]
    return None

def send_email(recipient, message):
    return f"Email sent to {recipient} with message: {message}"

tool_functions = {
    "get_inventory": get_inventory,
    "get_total_revenue": get_total_revenue,
    "get_top_product": get_top_product,
    "get_inventory_report": get_inventory_report,
    "send_email": send_email
}