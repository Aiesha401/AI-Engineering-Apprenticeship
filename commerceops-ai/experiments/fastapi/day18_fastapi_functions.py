from fastapi import FastAPI
from fastapi import HTTPException
from mini_projects.commerceops_agent.tools import get_inventory,get_total_revenue

app = FastAPI()

# def cube(number):
#     return number**3
# @app.get("/cube")
# def get_square(number: int):
#     return {
#         "number": number,
#         "cube": cube(number)
#     }
# products = [
#     "iPhone 16",
#     "Samsung S24",
#     "MacBook Air"
# ]

# @app.get("/products")
# def get_products():
#     return products

# inventory = {
#     "iPhone 16": 42,
#     "Samsung S24": 18
# }
# @app.get("/inventory")
# def get_inventory():
#     return inventory

# @app.get("/inventory/{product}")
# def inventory_lookup(product: str):
#     if product not in inventory:
#         raise HTTPException(
#             status_code=404,
#             detail="product not found"
#         )
#     return {
#         "product": product,
#         "quantity": inventory[product]
#     }

@app.get("/inventory/{product}")
def inventory(product: str):
    quantity = get_inventory(product)
    if quantity == "Product not found":
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return {
        "product":product,  
        "quantity":quantity
    }

@app.get("/revenue")
def revenue():
    return {
        "total_revenue": get_total_revenue()
    }