from pydantic import BaseModel
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)


patient_info1 = {'name': 'nitish', 'age': 21, 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '01888'}}
patient_info2 = {'name': 'nitish', 'age': 21, 'weight': 75.2, 'married': True, 'contact_details': {'email': 'abc@gmail.com', 'phone': '01888'}}


patient1 = Patient(**patient_info1)
patient2 = Patient(**patient_info2)

insert_patient_data(patient1)

update_patient_data(patient2)