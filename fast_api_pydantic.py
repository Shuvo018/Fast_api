from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)



patient_info1 = {'name': 'nitish', 'email': 'abc@gmail.com', 'linkedin_url': 'http://linkedin.com/1234', 'age': 21, 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '01888'}}
patient_info2 = {'name': 'nitish', 'email': 'abc@gmail.com', 'linkedin_url': 'http://linkedin.com/1234', 'age': 21, 'weight': 75.2, 'married': True, 'contact_details': {'email': 'abc@gmail.com', 'phone': '01888'}}


patient1 = Patient(**patient_info1)
patient2 = Patient(**patient_info2)

insert_patient_data(patient1)

update_patient_data(patient2)