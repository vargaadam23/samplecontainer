from fastapi import FastAPI

app = FastAPI()
#heloo
@app.get("/hello")
def read_hello():
    return {"name": "Hello tester"}
