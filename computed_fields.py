from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: Optional[List[str]]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/(self.height**2), 2)



def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)







patient_info1 = {'name': 'nitish', 'email': 'abc@gmail.com', 'linkedin_url': 'http://linkedin.com/1234', 
                 'age': 71, 'weight': 80.0, 'height': 1.85, 'married': True, 'allergies': ['pollen', 'dust'],
                   'contact_details': {'email': 'abc@gmail.com', 'phone': '01888233145'}}

patient1 = Patient(**patient_info1)
insert_patient_data(patient1)
