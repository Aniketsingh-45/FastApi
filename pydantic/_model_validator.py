from pydantic import BaseModel,EmailStr,AnyUrl,Field,model_validator
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

#model validator - to apply custom validation on model
    @model_validator(mode="after")
    def validate_emrgency_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact_detail:
            raise ValueError("Emergency contact is required for patients older than 60")

        return model

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


patient_info= {"name":"Aniket","email":"abc@gmail.com","linkedin":"https://www.linkedin.com/in/aniket-shinde-a1b2c3d4e5f6/", "age":65, "weight":12.5, "married":True, "allergies":["penicillin", "latex"], "contact_detail":{"phone":"1234567890", "emergency":"1234567890"}}
patient1=Patient(**patient_info)


updatepatient(patient1) 




    
