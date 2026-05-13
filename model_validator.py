from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]]
    contact_details: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 21 and 'phone' not in model.contact_details:
            raise ValueError('Patients older than 60 must have contact number')
        return model

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)







patient_info1 = {'name': 'nitish', 'email': 'abc@gmail.com', 'linkedin_url': 'http://linkedin.com/1234', 'age': 71, 'weight': 80.0, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '01888233145'}}

patient1 = Patient(**patient_info1)
insert_patient_data(patient1)
