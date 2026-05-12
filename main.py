from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def hello():
    return {"message": 'Hello world'}

@app.get('/about')
def about():
    return {"message": "Hi, i am learning fastapi"}

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data if data else "lsfjaslk"

@app.get("/view")
def view():
    return load_data()


# load(): json -> dict | read file
# dump(): dict -> json | write file
