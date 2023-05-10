from fastapi import FastAPI

app = FastAPI()


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    return {"result": num1 + num2}


@app.get("/subtract/{num1}/{num2}")
async def subtract(num1: int, num2: int):
    return {"result": num1 - num2}


@app.get("/multiply/{num1}/{num2}")
async def multiply(num1: int, num2: int):
    return {"result": num1 * num2}


@app.get("/divide/{num1}/{num2}")
async def divide(num1: int, num2: int):
    if num2 == 0:
        return {"error": "division by zero"}
    else:
        return {"result": num1 / num2}

