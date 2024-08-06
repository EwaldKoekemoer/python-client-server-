from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {
        "num1": 1,
        "num2": 2,
        "num3": 3
    }
