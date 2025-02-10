from fastapi import FastAPI

app = FastAPI()
#helo
@app.get("/hello")
def read_hello():
    return {"name": "Hello tester"}
