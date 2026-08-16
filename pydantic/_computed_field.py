from pydantic import BaseModel,EmailStr,AnyUrl,computed_field
from typing import List, Dict, Optional,Annotated


class Patient(BaseModel):
    name:str
    email:EmailStr #email validation
    linkedin:AnyUrl #url validation
    age:int 
    height:float #meter
    weight:float #kg
    married:bool
    allergies:List[str]
    contact_detail:Dict[str, str]

    @computed_field
    @property

    def bmi(self) ->float:
        bmi=round(self.weight/(self.height
        **2),2)

        return bmi


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
    print("BMI:",patient.bmi)
    print("updated") 


patient_info= {"name":"Aniket","email":"abc@gmail.com","linkedin":"https://www.linkedin.com/in/aniket-shinde-a1b2c3d4e5f6/", "age":65, "height":1.75, "weight":70, "married":True, "allergies":["penicillin", "latex"], "contact_detail":{"phone":"1234567890", "emergency":"1234567890"}}
patient1=Patient(**patient_info)


updatepatient(patient1) 




    
