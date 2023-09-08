from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Hello World!"}

@app.get("/whoami/{name}")
async def read_user(name):
    return {"Message": f"Hello {name} Welcome to Sourabh's Fast API test app. As far my knowledge you are a vary good human being who loves to help others."}