from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

address_dict = {'city': 'chattogram', 'state': 'mirsarai', 'pin': '1234'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Nitish', 'gender': 'male', 'age': 18, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.city)

# Batter organization of related data 
# Reusability: use vitals in mutiple models (Patient, MedicalRecord,...)
# Validation: Nested models are validated automatically no extra work needed