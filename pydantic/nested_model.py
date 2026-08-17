from pydantic import BaseModel

#nested model is a model inside a model


class Address(BaseModel):
    city:str
    pincode:str
    state:str


class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address


add={'city':'patna', 'pincode':'801503', 'state':'bihar'}

address1=Address(**add)

patient_dict={'name':'Rahul', 'gender':'Male', 'age':25, 'address':address1 }

patient1=Patient(**patient_dict) 

print(patient1)
print(patient1.address.city)
print(patient1.address.pincode)
print(patient1.address.state)