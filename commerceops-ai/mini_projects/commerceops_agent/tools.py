def get_inventory(product):
    inventory = {
        "iphone 16": 42,
        "samsung s24": 18,
        "macbook air": 9
    }

    return inventory.get(product.lower(), "Product not found")
def get_inventory_report():
    return{
        "iphone 16": 42,
        "samsung s24": 18,
        "macbook air": 9
    }
def get_total_revenue():
    return "$12,500"

def get_top_product():
    return "iPhone 16"


def send_email(recipient, message):
    return f"Email sent to {recipient} with message: {message}"

tool_functions = {
    "get_inventory": get_inventory,
    "get_total_revenue": get_total_revenue,
    "get_top_product": get_top_product,
    "get_inventory_report": get_inventory_report,
    "send_email": send_email
}