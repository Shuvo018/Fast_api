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

print(type(patient1))
print(patient1)

temp = patient1.model_dump() # dict
print(type(temp))
print(temp)

temp = patient1.model_dump_json() # str
print(type(temp))
print(temp)


temp = patient1.model_dump(include=['name'])
print(temp)
temp = patient1.model_dump(exclude=['name'])
print(temp)
