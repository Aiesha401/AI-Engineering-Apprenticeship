import sqlite3


connection = sqlite3.connect(
    "mini_projects/commerceops_agent/commerceops.db",
    check_same_thread=False
)

cursor = connection.cursor()


def get_inventory(product):
    cursor.execute(
        """
        SELECT quantity
        FROM inventory
        WHERE LOWER(product) = LOWER(?)
        """,
        (product,)
    )

    row = cursor.fetchone()

    if row:
        return row[0]

    return "Product not found"


def get_inventory_report():
    cursor.execute(
        """
        SELECT product, quantity
        FROM inventory
        """
    )

    rows = cursor.fetchall()

    report = {}

    for product, quantity in rows:
        report[product] = quantity

    return report


def get_total_revenue():
    cursor.execute(
        """
        SELECT SUM(quantity * price)
        FROM inventory
        """
    )

    row = cursor.fetchone()

    if row:
        return f"${row[0]:,.2f}"

    return "$0.00"


def get_top_product():
    cursor.execute(
        """
        SELECT product
        FROM inventory
        ORDER BY quantity DESC
        LIMIT 1
        """
    )

    row = cursor.fetchone()

    if row:
        return row[0]

    return None


def send_email(recipient, message):
    return f"Email sent to {recipient} with message: {message}"


tool_functions = {
    "get_inventory": get_inventory,
    "get_inventory_report": get_inventory_report,
    "get_total_revenue": get_total_revenue,
    "get_top_product": get_top_product,
    "send_email": send_email
}