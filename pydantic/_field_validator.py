from pydantic import BaseModel,EmailStr,AnyUrl,Field, field_validator
from typing import List, Dict, Optional,Annotated


class Patient(BaseModel):
    name:str
    email:EmailStr #email validation
    linkedin:AnyUrl #url validation
    age:int 
    weight:float
    married:bool
    allergies:List[str]
    contact_detail:Dict[str, str]

# field validator -  to apply custom validation on field
    @field_validator('email')
    @classmethod

    def email_validator(cls,value):
        valid_domain=['hdfc.com','icici.com',]

        domain_name=value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('invalid email domain')

        return value


    @field_validator("name")
    @classmethod

    def name_validator(cls, value):
        return value.upper()


    @field_validator("age", mode='after')
    @classmethod

    def age_validator(cls,value):
        if 0<value<100:
            return value
        
        else:
            raise ValueError("age should be in range of 1 to 99")



  

def insertpatient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.linkedin)
    print("inserted")



def updatepatient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.email)
    print(patient.linkedin)
    print(patient.weight)
    print("updated") 


patient_info= {"name":"Aniket","email":"abc@icici.com","linkedin":"https://www.linkedin.com/in/aniket-shinde-a1b2c3d4e5f6/", "age":"30", "weight":12.5, "married":True, "allergies":["penicillin", "latex"], "contact_detail":{"phone":"1234567890"}}


patient1=Patient(**patient_info) 


updatepatient(patient1) 




    
