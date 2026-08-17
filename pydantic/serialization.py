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

temp=patient1.model_dump(include=['name','age'])
print(temp)
print(type(temp))



temp1=patient1.model_dump_json()
print(temp1)
print(type(temp1))  