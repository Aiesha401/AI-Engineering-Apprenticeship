from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI"}

@app.get("/hello/{name}")
def home(name: str):
    return {"message": f"Hello {name}!"}

@app.get("/square")
def home(number: int):
    return {
        "number" : number,
        "square" : number*number
    }

@app.get("/inventory/{product}")
def home(product: str):
    return {
        "product": product,
        "status" : "API working"
    }