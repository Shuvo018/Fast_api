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
# load(): json -> dict | read file
# dump(): dict -> json | write file

    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data if data else "not found"

@app.get("/view")
def view():
    return load_data()

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error': 'patient not found'}
    