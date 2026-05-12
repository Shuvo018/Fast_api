from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)


patient_info = {'name': 'nitish', 'age': 21}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

update_patient_data(patient1)