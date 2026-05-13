from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=1, lt=25)
    weight: Annotated[float, Field(gt=1, strict=True, description="The weight must be greater than one")]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
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



patient_info1 = {'name': 'nitish', 'email': 'abc@gmail.com', 'linkedin_url': 'http://linkedin.com/1234', 'age': 21, 'weight': 80.0, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '01888'}}
patient_info2 = {'name': 'nitish', 'email': 'abc@gmail.com', 'linkedin_url': 'http://linkedin.com/1234', 'age': 21, 'weight': 75.2, 'married': True, 'contact_details': {'email': 'abc@gmail.com', 'phone': '01888'}}


patient1 = Patient(**patient_info1)
patient2 = Patient(**patient_info2)

insert_patient_data(patient1)

# update_patient_data(patient2)